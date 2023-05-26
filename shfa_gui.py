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
            command=self.on_press)
        button.grid(row=0, column=0)

    def on_press(self):
        """Обработка нажатия кнопки."""

        filename = askopenfilename(
            title="Выбор файла для закодирования"
        )

        if not filename:
            return

        output = tkinter.filedialog.asksaveasfilename(
            title="Выбор файла для сохранения",
            confirmoverwrite=False
        )

        if not output:
            return

        try:
            reader = Reader(filename)
            data = reader.read()

            writer = CompressionWriter(data, output)
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            return

        try:
            writer.write()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            return

        tkinter.messagebox.showinfo(title="Успешно",
                                    message=f"Сжатая информация записана в {output}")


class DecodeButton:
    """Кнопка декодирования файла."""

    def __init__(self, root_frame):
        self.root = root_frame
        button = ttk.Button(
            root_frame,
            text="Декодировать",
            command=self.on_press)
        button.grid(row=1, column=0)

    def on_press(self):
        """Обработка нажатия на кнопку."""

        filename = askopenfilename()

        if not filename:
            return

        output = tkinter.filedialog.asksaveasfilename(
            title="Выбор файла для сохранения",
            confirmoverwrite=False
        )

        if not output:
            return

        data = None

        try:
            reader = DecompressionReader(filename)
            data = reader.read()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            return

        try:
            writer = Writer(data, output)
            writer.write()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            return

        tkinter.messagebox.showinfo(title="Успешно",
                                    message=f"Расжатая информация записана в {output}")


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
