#!/usr/bin/env python3

import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from writer import CompressionWriter, Writer
from reader import DecompressionReader, Reader


class EncodeButton:
    def __init__(self, root_frame):
        self.root = root_frame
        ttk.Button(root_frame, text="Закодировать", command=self.encode).pack()

    def encode(self):
        self.filename = askopenfilename()

        if not self.filename:
            return

        self.inp=tkinter.Toplevel(self.root)
        self.inp.title("Файл вывода")

        e = tkinter.Entry(master=self.inp, text='Укажите название файла')
        e.grid(row=0,column=0)
        e.focus()

        e.bind("<Return>", self.on_pressed) 

    def on_pressed(self, event):
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
    def __init__(self, root_frame):
        self.root = root_frame
        ttk.Button(root_frame, text="Декодировать", command=self.decode).pack()

    def decode(self):
        self.filename = askopenfilename()

        if not self.filename:
            return

        self.inp=tkinter.Toplevel(self.root)
        self.inp.title("Файл вывода")

        e = tkinter.Entry(self.inp, text="Укажите имя файла")
        e.grid(row=0,column=0)
        e.focus()

        e.bind("<Return>", self.on_pressed) 

    def on_pressed(self, event):
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
    def __init__(self):
        super().__init__(tkinter.Tk())

        self.master.title("ShFa")
        self.master.resizable(width=False, height=False)

        EncodeButton(self)
        DecodeButton(self)

        self.pack()

if __name__ == '__main__':
    ShannonFanoApplication().mainloop()