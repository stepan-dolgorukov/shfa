#!/usr/bin/env python3

import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from writer import CompressionWriter, Writer
from reader import DecompressionReader, Reader
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def on_press(self):
        raise NotImplementedError

class Button(ABC):
    """Класс абстрактный «кнопка»."""

    @abstractmethod
    def on_press(self):
        """Действия, которые выполнятся, когда пользователь нажмёт на кнопку."""

        raise NotImplementedError

class EncodeButton(Button):
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

        input_fname = askopenfilename(
            title="Выбор файла для закодирования"
        )

        if not input_fname:
            return

        output_fname = tkinter.filedialog.asksaveasfilename(
            title="Выбор файла для сохранения",
            confirmoverwrite=False
        )

        if not output_fname:
            return

        try:
            reader = Reader(input_fname)
            data = reader.read()

            writer = CompressionWriter(data, output_fname)
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            return

        try:
            writer.write()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            return

        tkinter.messagebox.showinfo(title="Успешно",
                                    message=f"Сжатая информация записана в {output_fname}")


class DecodeButton(Button):
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

        input_fname = askopenfilename()

        if not input_fname:
            return

        output_fname = tkinter.filedialog.asksaveasfilename(
            title="Выбор файла для сохранения",
            confirmoverwrite=False
        )

        if not output_fname:
            return

        data = None

        try:
            reader = DecompressionReader(input_fname)
            data = reader.read()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            return

        try:
            writer = Writer(data, output_fname)
            writer.write()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            return

        tkinter.messagebox.showinfo(title="Успешно",
                                    message=f"Расжатая информация записана в {output_fname}")


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
