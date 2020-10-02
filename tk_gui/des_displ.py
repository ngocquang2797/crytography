from tkinter import *
from alg.sha512 import sha512
from tk_gui.sha512_displ import Sha512_displ
import tkinter.messagebox

class des_disl(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.plaintxt = StringVar()
        self.key = StringVar()
        self.init_window()

    def init_window(self):
        self.plaintxt.set("")

        # self.pack(fill=BOTH, expand=1)
        plain_txt = Label(self, text="Plaintext")
        plain_txt.grid(row=0, column=1, padx=30, pady=30)
        # self.plaintxt.trace("w", self.decode)
        self.plain_txt_box = Entry(self, textvariable=self.plaintxt, width=150)
        self.plain_txt_box.grid(row=0, column=2)

        key_txt = Label(self, text="Key")
        key_txt.grid(row=1, column=1)
        self.key_txt_box = Entry(self, textvariable=self.key, width=150)
        self.key_txt_box.grid(row=1, column=2)
        self.key_gen_btn = Button(self, text="Gen Key", command=self.gen_key)
        self.key_gen_btn.grid(row=1, column=3)

    def gen_key(self):
        if (len(self.key.get()) <= 8):
            print("True")
            top = Toplevel()
            top.grab_set()

        else:
            tkinter.messagebox.showerror('XXX', 'Key need 64-bit length')

    # def key_gen_window(self):