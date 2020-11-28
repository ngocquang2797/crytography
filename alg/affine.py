def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

class Affine(object):
    # Ma hoa
    def encry(self, plaintxt, key):
        return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                            + ord('A')) for t in plaintxt.upper().replace(' ', '')])

    # Giai ma
    def decry(self, cipher, key):
        return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
                             % 26) + ord('A')) for c in cipher])

if __name__ == "__main__":
    print("Nhap ban tin ro: ")
    plt = input()
    k = []
    print("Nhap khoa k1: ")
    k.append(int(input()))
    print("Nhap khoa k2: ")
    k.append(int(input()))
    A = Affine
    print("Ban tin duoc ma hoa: " + A.encry(A, plt, k))