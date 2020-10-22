
# from tkinter import *
#
# root = Tk()
#
# def key(event):
#     print("pressed", repr(event.char))
#
# def callback(event):
#     frame.focus_set()
#     print("clicked at", event.x, event.y)
#
# frame = Frame(root, width=100, height=100)
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.pack()
#
# root.mainloop()
import tkinter as tk
import re

class EntryFormular(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)

        self.entrylist = [
        "entry 1",
        "entry 2",
        "entry 3"
        ]

        self.inputvars = list()
        self.build()

    def build(self):

        for entry in self.entrylist:

            var = tk.StringVar(self.master)
            var.trace("w",self.validateFloatInput)
            element = tk.Entry(self,textvariable=var)
            element.pack()
            self.inputvars.append(var)

    def validateFloatInput(self,name,index,mode):

        regex = re.compile(r'^0(\.\d+)?|1(\.0?)?$')

        for var in self.inputvars:
            if name == str(var):
                if regex.match(var.get()):
                    pass
                else:
                    var.set(var.get()[:-1])
                    self.master.bell()

class Application:
    def __init__(self, master):
        self.master = master
        self.entryformular = EntryFormular(master)
        self.entryformular.pack()


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = Application(root)
    root.mainloop()