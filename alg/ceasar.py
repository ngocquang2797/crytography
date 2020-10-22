
class Ceasar(object):

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

text = "CEASER CIPHER DEMo"
crtxt = "GIEWIV GMTLIV HIQs"
s = 4
txt = Ceasar
print(txt.encryp(txt, plaintxt=text, k=s))
print(txt.decryp(txt, plaintxt=crtxt, k=s))