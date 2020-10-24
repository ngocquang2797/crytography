
class Ceasar(object):
    def __init__(self):
        self.k = 3

    def encryp(self, plaintxt):
        enc = ""
        for c in plaintxt:
            if (c.isupper()):
                enc += chr((ord(c) + self.k - 65) % 26 + 65)
            elif (c.isspace()):
                enc += " "
            else:
                enc += chr((ord(c) + self.k - 97) % 26 + 97)
        return enc

    def decryp(self, cipher):
        plt = ""
        for c in cipher:
            if (c.isupper()):
                plt += chr((ord(c) - self.k - 65) % 26 + 65)
            elif(c.isspace()):
                plt += " "
            else:
                print("S")
                plt += chr((ord(c) - self.k - 97) % 26 + 97)
        return plt

if __name__ == "__main__":
    # text = "CEASER CIPHER DEMo"
    # crtxt = "GIEWIV GMTLIV HIQs"
    # s = 4
    print("Nhap ban tin ro: ")
    text = input()
    txt = Ceasar()
    print("Ban tin duoc ma hoa: " + txt.encryp(plaintxt=text))