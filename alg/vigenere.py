
class Vegenere(object):
    def key_stream(self, key):
        k_s = []
        for i in range(len(key)):
            if key.isupper():
                k_s.append(ord(key[i])-65)
            else:
                k_s.append(ord(key[i])-97)
        return k_s

    def encry(self, plaintxt, key):
        cipher = ""
        k = self.key_stream(self, key)
        for i in range(len(plaintxt)):
            if plaintxt[i].isupper():
                cipher += chr((ord(plaintxt[i]) + (k[i%len(k)]) - 65) % 26 + 65)
            else:
                cipher += chr((ord(plaintxt[i]) + (k[i%len(k)]) - 97) % 26 + 65)

        return cipher

    def decry(self, cipher, key):
        plaintxt = ""

plt = "sheislistening"
k = "PASCAL"
cp = "PASCAL"
C = Vegenere
print(C.encry(C, plt, k))
# print(C.decry(C, cp, k))