#!/usr/bin/env python3

import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from writer import CompressionWriter
from reader import DecompressionReader

def encode():
    filename = askopenfilename()

    if not filename:
        tkinter.messagebox.showerror(title="Ошибка", message="Файл не выбран")
        return

    inp=tkinter.Tk()
    inp.title("Файл вывода")

    data = ""
    with open(filename, 'rb') as file:
        data = file.read()

    e = tkinter.Entry(inp, text='Укажите название файла')
    e.grid(row=0,column=0)
    e.focus()

    def on_pressed(output):

        try:
            writer = CompressionWriter(data, output)
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            inp.destroy()
            return

        try:
            writer.write()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            inp.destroy()
            return

        tkinter.messagebox.showinfo(title="Успешно",
            message=f"Сжатая информация записана в {output}")

        inp.destroy()


    b = tkinter.Button(inp, text='Sub',command=lambda: on_pressed(e.get()))
    b.grid(row=0, column=1)


def decode():
    filename = askopenfilename()

    if not filename:
        tkinter.messagebox.showerror(title="Ошибка", message="Файл не выбран")
        return

    inp=tkinter.Tk()
    inp.title("Файл вывода")

    e = tkinter.Entry(inp, text="Укажите имя файла")
    e.grid(row=0,column=0)
    e.focus()

    def on_pressed(output):
        data = None

        try:
            reader = DecompressionReader(filename)
            data = reader.read()
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            inp.destroy()
            return

        try:
            with open(output, "wb") as out:
                out.write(data)
        except Exception as exc:
            tkinter.messagebox.showerror(title="Ошибка", message=exc)
            inp.destroy()
            return

        tkinter.messagebox.showinfo(title="Успешно",
            message=f"Расжатая информация записана в {output}")

        inp.destroy()

    b = tkinter.Button(inp, text='Sub',command=lambda: on_pressed(e.get()))
    b.grid(row=0, column=1)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("ShFa")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    ttk.Button(frm, text="Enc", command=encode).grid(column=0, row=0)
    ttk.Button(frm, text="Dec", command=decode).grid(column=1, row=0)

    root.mainloop()