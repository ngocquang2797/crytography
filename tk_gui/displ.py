from tkinter import *
#
class Sha512_displ(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.init_window()
        self.plaintxt = StringVar()

    # Creation of init_window
    def init_window(self):
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        


    #
#
#
# root = Tk()
#
# #size of the window
# root.geometry("400x300")
#
# app = Window(root)
# root.mainloop()
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("400x300")
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = Sha512_displ()
# tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='SHA-512')
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1, text="Welcome to GeeksForGeeks").grid(column=0, row=0, padx=30, pady=30)
# ttk.Label(tab2).grid(column=0, row=0, padx=30, pady=30)

root.mainloop()
