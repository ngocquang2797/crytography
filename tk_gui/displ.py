from tkinter import *
from alg.sha512 import sha512
from tk_gui.sha512_displ import Sha512_displ
from tk_gui.des_displ import des_disl
import tkinter.messagebox

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.geometry("1200x600")
    root.title("Tab Widget")
    root.iconbitmap("f:/Code/Python/crytography/icon/HUST.ico")
    tabControl = ttk.Notebook(root)

    tab1 = des_disl()
    tab2 = Sha512_displ()
    # tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='DES')
    tabControl.add(tab2, text='SHA-512')
    tabControl.pack(expand=1, fill="both")

    root.update()
    root.mainloop()


if __name__ == "__main__":
    main()