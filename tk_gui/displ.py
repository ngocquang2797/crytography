from tkinter import *
from alg.sha512 import sha512
import tkinter.messagebox
#
class Sha512_displ(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.plaintxt = StringVar()
        self.decodetxt = ""
        self.init_window()

    def decode(self, *args):
        # print(self.plaintxt.get())
        self.decodetxt = sha512(self.plaintxt.get()).digest()
        self.code_txt_box.configure(state="normal")
        self.code_txt_box.delete(0, 'end')
        self.code_txt_box.insert(index=1, string=self.decodetxt)
        self.code_txt_box.configure(state="readonly")

    # Creation of init_window
    def init_window(self):
        self.plaintxt.set("")

        self.pack(fill=BOTH, expand=1)
        plain_txt = Label(self, text="Plaintext")
        plain_txt.grid(row=0, column=1, padx=30, pady=30)
        self.plaintxt.trace("w", self.decode)
        self.plain_txt_box = Entry(self, textvariable=self.plaintxt, width=150)
        self.plain_txt_box.grid(row=0, column=2)

        self.decodetxt = sha512("").digest()
        code_txt = Label(self, text="Encoded")
        code_txt.grid(row=1, column=1)
        self.code_txt_box = Entry(self, textvariable=self.decodetxt, width=150)
        self.code_txt_box.insert(index=0, string=self.decodetxt)
        self.code_txt_box.configure(state="readonly")
        self.code_txt_box.grid(row=1, column=2)

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

    def checkKeyLen(self):
        if(len(self.key.get())<=8):
            return True
        else:
            return False

    def gen_key(self):
        if (len(self.key.get()) <= 8):
            print("True")
        else:
            tkinter.messagebox.showerror('XXX', 'Key need 64-bit length')

    def key_gen_window(self):


import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.geometry("1200x600")
    root.title("Tab Widget")
    tabControl = ttk.Notebook(root)

    tab1 = des_disl()
    tab2 = Sha512_displ()
    # tab2 = ttk.Frame(tabControl)

    tabControl.add(tab2, text='SHA-512')
    tabControl.add(tab1, text='Tab 1')
    tabControl.pack(expand=1, fill="both")

    root.update()
    root.mainloop()


if __name__ == "__main__":
    main()