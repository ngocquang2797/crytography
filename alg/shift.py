
class Shift(object):
    def __init__(self):
        self.k = 3

    def encryp(self, plaintxt, k):
        enc = ""
        for c in plaintxt:
            if (c.isupper()):
                enc += chr((ord(c) + k - 65) % 26 + 65)
            elif (c.isspace()):
                enc += " "
            else:
                enc += chr((ord(c) + k - 97) % 26 + 97)
        return enc

    def decryp(self, plaintxt, k):
        dec = ""
        for c in plaintxt:
            if (c.isupper()):
                dec += chr((ord(c) - k - 65) % 26 + 65)
            elif(c.isspace()):
                dec += " "
            else:
                print("S")
                dec += chr((ord(c) - k - 97) % 26 + 97)
        return dec

if __name__ == "__main__":
    # text = "CEASER CIPHER DEMo"
    # crtxt = "GIEWIV GMTLIV HIQs"
    # s = 4
    print("Nhap ban tin ro: ")
    text = input()
    print("Nhap khoa k: ")
    key = int(input())
    txt = Shift
    print("Ban tin duoc ma hoa: " + txt.encryp(txt, plaintxt=text, k=key))