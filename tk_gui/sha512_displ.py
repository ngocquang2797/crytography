from tkinter import *
from alg.sha512 import sha512
import tkinter.messagebox
#
class Sha512_displ(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.plaintxt = StringVar()
        self.decodetxt = ""
        self.optioncode = StringVar()
        self.optioncode.set("ASCII")
        self.init_window()

    def decode(self, *args):
        # print(self.plaintxt.get())
        self.decodetxt = sha512(self.plaintxt.get(), self.optioncode.get()).digest()
        self.code_txt_box.configure(state="normal")
        self.code_txt_box.delete(0, 'end')
        self.code_txt_box.insert(index=1, string=self.decodetxt)
        self.code_txt_box.configure(state="readonly")

    def keyPress(self, event):
        if self.optioncode.get() == "BIN":
            if event.char in ('0', '1'):
                print(event.char)
            elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace'):
                # print(event.keysym)
                return 'break'
        elif self.optioncode.get() == "HEX":
            if event.char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'):
                print(event.char)
            elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace'):
                return 'break'

    def resetplaintxt(self, *args):
        self.plaintxt.set("")
        self.plain_txt_box.delete(0, 'end')

    # Creation of init_window
    def init_window(self):
        self.plaintxt.set("")

        self.pack(fill=BOTH, expand=1)
        plain_txt = Label(self, text="Plaintext")
        plain_txt.grid(row=0, column=1, padx=30, pady=30)
        self.plaintxt.trace("w", self.decode)
        self.plain_txt_box = Entry(self, textvariable=self.plaintxt, width=150)
        self.plain_txt_box.bind('<KeyPress>', self.keyPress)
        self.plain_txt_box.grid(row=0, column=2)

        drop = OptionMenu(self, self.optioncode, *["ASCII", "HEX", "BIN"], command=self.resetplaintxt)
        drop.grid(row=0, column=3)

        self.decodetxt = sha512("").digest()
        code_txt = Label(self, text="Encoded")
        code_txt.grid(row=1, column=1)
        self.code_txt_box = Entry(self, textvariable=self.decodetxt, width=150)
        self.code_txt_box.insert(index=0, string=self.decodetxt+self.optioncode.get())
        self.code_txt_box.configure(state="readonly")
        self.code_txt_box.grid(row=1, column=2)