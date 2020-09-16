
Ch  = lambda x, y, z: (z ^ (x & (y ^ z)))
Maj = lambda x, y, z: (((x | y) & z) | (x & y))


H = ["6A09E667F3BCC908",
     "BB67AE8584CAA73B",
     "3C6EF372FE94F82B",
     "A54FF53A5F1D36F1",
     "510E527FADE682D1",
     "9B05688C2B3E6C1F",
     "1F83D9ABFB41BD6B",
     "5BE0CD19137E2179"]


def input_format(m):
    input_mess_ascii_hex = ''.join(str(hex(ord(c))[2:]) for c in m)
    len_of_mess = hex(len(m) * 8)[2:].zfill(32)
    num_block = int((len(input_mess_ascii_hex) + len(len_of_mess)) / 256) + 1
    return  input_mess_ascii_hex + "80" + len_of_mess.zfill(256 * num_block - 2 - len(input_mess_ascii_hex))

def hash_buffer_initialization(mess, numblock):
    block_mess = [mess[i*256:i*256+256] for i in range(numblock)]
    print(block_mess)
    return block_mess
    # for c in block_mess:
    #     print(c)

def word_expansion(block_mess):
    W = [block_mess[i*16:i*16+16] for i in range(16)]
    print(W)

input_mess = input()
x = input_format(input_mess)
print(x)
print(len(x))
# blockmess = hash_buffer_initialization(mes, nu)
# word_expansion(blockmess[0])