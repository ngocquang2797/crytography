import tkinter as tk

def keyPress(event):
    if event.char in ('0', '1'):
        print(event.char)
        print(txt.get())
    elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace'):
        print(event.keysym)

        return 'break'


root = tk.Tk()
txt = tk.StringVar()
entry = tk.Entry(textvariable=txt)
entry.bind('<KeyPress>', keyPress)
entry.pack()
entry.focus()

root.mainloop()