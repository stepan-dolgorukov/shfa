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
        button = ttk.Button(
            root_frame,
            text="Закодировать",
            command=self.encode)
        button.grid(row=0, column=0)

    def encode(self):
        """Обработка нажатия кнопки."""

        self.filename = askopenfilename()

        if not self.filename:
            return

        self.output_file_window = tkinter.Toplevel(self.root)
        self.output_file_window.title("Файл вывода")
        self.output_file_window.geometry("200x50")

        output_file_entry = tkinter.Entry(
            master=self.output_file_window,
            text='Укажите название файла')
        output_file_entry.grid(row=0, column=0)
        output_file_entry.focus()
        output_file_entry.bind("<Return>", self.on_return)

    def on_return(self, event):
        """Обработка ввода имени файла выхода."""

        output = event.widget.get()

        try:
            reader = Reader(self.filename)
            data = reader.read()

            writer = CompressionWriter(data, output)
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            self.output_file_window.destroy()
            return

        try:
            writer.write()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            self.output_file_window.destroy()
            return

        tkinter.messagebox.showinfo(title="Успешно",
                                    message=f"Сжатая информация записана в {output}")

        self.output_file_window.destroy()


class DecodeButton:
    """Кнопка декодирования файла."""

    def __init__(self, root_frame):
        self.root = root_frame
        button = ttk.Button(
            root_frame,
            text="Декодировать",
            command=self.decode)
        button.grid(row=1, column=0)

    def decode(self):
        """Обработка нажатия на кнопку."""

        self.filename = askopenfilename()

        if not self.filename:
            return

        self.output_file_input_window = tkinter.Toplevel(self.root)
        self.output_file_input_window.title("Файл вывода")
        self.output_file_input_window.geometry("200x50")

        output_file_entry = tkinter.Entry(
            self.output_file_input_window,
            text="Укажите имя файла")
        output_file_entry.grid(row=0, column=0)
        output_file_entry.focus()

        output_file_entry.bind("<Return>", self.on_return)

    def on_return(self, event):
        """Обработка ввода пользователем имени файла вывода."""

        output = event.widget.get()
        data = None

        try:
            reader = DecompressionReader(self.filename)
            data = reader.read()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            self.output_file_input_window.destroy()
            return

        try:
            writer = Writer(data, output)
            writer.write()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            self.output_file_input_window.destroy()
            return

        tkinter.messagebox.showinfo(title="Успешно",
                                    message=f"Расжатая информация записана в {output}")

        self.output_file_input_window.destroy()


class ShannonFanoApplication(tkinter.Frame):
    """Приложение с графическим интерфейсом «Архиватор Shannon-Fano»."""

    def __init__(self):
        master_window = tkinter.Tk()
        master_window.geometry("200x100")

        super().__init__(master_window)

        self.master.title("ShFa")
        self.master.resizable(width=False, height=False)

        EncodeButton(self)
        DecodeButton(self)

        self.pack()


if __name__ == '__main__':
    ShannonFanoApplication().mainloop()
