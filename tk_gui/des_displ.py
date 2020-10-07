from tkinter import *
from alg.sha512 import sha512
from tk_gui.sha512_displ import Sha512_displ
from alg.des import DES
import tkinter.messagebox

def LS(key, n):
    return key[n:] + key[:n]

pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

pc2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

numls = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def createTable(root, txt, row, col, spanx = 1, width = 20):
    t = Entry(root, width=width+spanx-1, fg='black')
    t.grid(row=row, column=col, columnspan=spanx)
    t.insert(END, txt)

class encrypt_disl(Toplevel):
    def __init__(self, plaintxt, key, opt_code="HEX"):
        Toplevel.__init__(self)
        self.encrypt = DES(plaintxt, key, opt_code)
        ECinfo = self.encrypt.getInfo()
        rouKey = self.encrypt.getKey()
        # print(ECinfo)
        # print(ECinfo[0][2])
        createTable(self, "Plain text: " + plaintxt, 0, 0, 4, 80)
        createTable(self, "After IP: "+ hex(int(ECinfo[0][1], 2))[2:], 1, 0, 4, 80)
        createTable(self, "L0: "+hex(int(ECinfo[0][2][0], 2))[2:], 2, 0, 2, 40)
        createTable(self, "R0: "+hex(int(ECinfo[0][3][0], 2))[2:], 2, 2, 2, 40)
        ttl = ["Round", "Left", "Right", "Round Key"]

        for i in range(4):
            createTable(self, ttl[i], 3, i)

        for i in range(16):
            createTable(self, "Round "+str(i+1), i+4, 0)
            createTable(self, hex(int(ECinfo[0][2][i+1], 2))[2:], i + 4, 1)
            createTable(self, hex(int(ECinfo[0][3][i+1], 2))[2:], i + 4, 2)
            createTable(self, hex(int(rouKey[i+1], 2))[2:], i + 4, 3)

        createTable(self, "After combination: "+hex(int(ECinfo[0][3][16], 2))[2:]+hex(int(ECinfo[0][2][16], 2))[2:], 20, 0, 4, 80)
        createTable(self, "Ciphertext: " + hex(int(ECinfo[0][4], 2))[2:], 21, 0, 4, 80)

class key_disl(Toplevel):
    def __init__(self, key):
        Toplevel.__init__(self)
        self.keys = "".join(str(bin(int(c, 16))[2:].zfill(4)) for c in key)
        print(len(self.keys))
        createTable(self, "Key: " + key, 0, 0, 4, 80)
        ttl = ["Round", "Left", "Right", "Round Key"]
        for i in range(len(ttl)):
            createTable(self, ttl[i], 1, i)

        self.keygen = "".join(self.keys[pc1[i] - 1] for i in range(56))
        self.C, self.D = [self.keygen[0][:28]], [self.keygen[0][28:]]
        keygen = [[], [], [], []]
        keygen[0].append("Round 0")
        keygen[1].append(self.keygen[:28])
        keygen[2].append(self.keygen[28:])
        keygen[3].append(self.keygen)
        for i in range(16):
            keygen[0].append("Round " + str(i + 1))
            keygen[1].append(LS(keygen[1][i], numls[i]))
            keygen[2].append(LS(keygen[2][i], numls[i]))
            k = keygen[1][i + 1] + keygen[2][i + 1]
            keygen[3].append("".join(k[pc2[j] - 1] for j in range(48)))
            for j in range(4):
                if j == 0:
                    createTable(self, keygen[j][i + 1], i+2, j)
                else:
                    createTable(self, hex(int(keygen[j][i + 1], 2))[2:], i + 2, j)

class des_disl(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.optioncode = StringVar()
        self.optioncode.set("HEX")
        self.plaintxt = StringVar()
        self.key = StringVar()
        self.init_window()

    def keyPress(self, event):
        if self.optioncode.get() == "BIN":
            if event.char in ('0', '1'):
                print(event.char)
            elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace'):
                return 'break'
        elif self.optioncode.get() == "HEX":
            if event.char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'):
                print(event.char)
            elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace'):
                return 'break'

    def init_window(self):
        self.plaintxt.set("")

        # self.pack(fill=BOTH, expand=1)
        plain_txt = Label(self, text="Plaintext")
        plain_txt.grid(row=0, column=1, padx=30, pady=30)
        # self.plaintxt.trace("w", self.decode)
        self.plain_txt_box = Entry(self, textvariable=self.plaintxt, width=150)
        self.plain_txt_box.bind('<KeyPress>', self.keyPress)
        self.plain_txt_box.grid(row=0, column=2)

        key_txt = Label(self, text="Key")
        key_txt.grid(row=1, column=1)
        self.key_txt_box = Entry(self, textvariable=self.key, width=150)
        self.key_txt_box.bind('<KeyPress>', self.keyPress)
        self.key_txt_box.grid(row=1, column=2)

        self.key_gen_btn = Button(self, text="Gen Key", command=self.gen_key)
        self.key_gen_btn.grid(row=1, column=3)

        self.encrypt = Button(self, text="Encryption", command=self.encryption)
        self.encrypt.grid(row=3, column=2)

    def encryption(self):
        if True:
            en = encrypt_disl(self.plaintxt.get(), self.key.get())
            # en = encrypt_disl("123456abcd132536", "aabb09182736ccdd")
            en.geometry("600x700")
            en.grab_set()

    def gen_key(self):
        if (len(self.key.get()) <= 16):
            print("True")
            top = key_disl(self.key.get())
            # top = key_disl("aabb09182736ccdd")
            top.geometry("600x700")
            top.grab_set()


        else:
            tkinter.messagebox.showerror('XXX', 'Key need 64-bit length')