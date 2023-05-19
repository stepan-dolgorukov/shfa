#!/usr/bin/env python3

import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from writer import CompressionWriter, Writer
from reader import DecompressionReader, Reader


class EncodeButton:
    """Кнопка кодирования файла."""

    def __init__(self, root_frame):
        self.root = root_frame
        button = ttk.Button(root_frame, text="Закодировать", command=self.encode)
        button.grid(row=0, column=0)

    def encode(self):
        """Обработка нажатия кнопки."""

        self.filename = askopenfilename()

        if not self.filename:
            return

        self.inp=tkinter.Toplevel(self.root)
        self.inp.title("Файл вывода")

        e = tkinter.Entry(master=self.inp, text='Укажите название файла')
        e.grid(row=0,column=0)

        e.focus()

        e.bind("<Return>", self.on_return) 

    def on_return(self, event):
        """Обработка ввода имени файла выхода."""

        output = event.widget.get()

        try:
            reader = Reader(self.filename)
            data = reader.read()

            writer = CompressionWriter(data, output)
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            self.inp.destroy()
            return

        try:
            writer.write()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            self.inp.destroy()
            return

        tkinter.messagebox.showinfo(title="Успешно",
            message=f"Сжатая информация записана в {output}")

        self.inp.destroy()

class DecodeButton:
    """Кнопка декодирования файла."""

    def __init__(self, root_frame):
        self.root = root_frame
        button = ttk.Button(root_frame, text="Декодировать", command=self.decode)
        button.grid(row=1, column=0)

    def decode(self):
        """Обработка нажатия на кнопку."""

        self.filename = askopenfilename()

        if not self.filename:
            return

        self.inp=tkinter.Toplevel(self.root)
        self.inp.title("Файл вывода")

        e = tkinter.Entry(self.inp, text="Укажите имя файла")
        e.grid(row=0,column=0)
        e.focus()

        e.bind("<Return>", self.on_return) 

    def on_return(self, event):
        """Обработка ввода пользователем имени файла вывода."""

        output = event.widget.get()
        data = None

        try:
            reader = DecompressionReader(self.filename)
            data = reader.read()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            self.inp.destroy()
            return

        try:
            writer = Writer(data, output)
            writer.write()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            self.inp.destroy()
            return

        tkinter.messagebox.showinfo(title="Успешно",
            message=f"Расжатая информация записана в {output}")

        self.inp.destroy()



class ShannonFanoApplication(tkinter.Frame):
    """Приложение с графическим интерфейсом «Архиватор Shannon-Fano»."""

    def __init__(self):
        master_window = tkinter.Tk()
        master_window.geometry("200x100")

        super().__init__(master_window)

        self.master.title("ShFa")

        EncodeButton(self)
        DecodeButton(self)

        self.pack()

if __name__ == '__main__':
    ShannonFanoApplication().mainloop()