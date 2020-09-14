
H = ["6A09E667F3BCC908",
     "BB67AE8584CAA73B",
     "3C6EF372FE94F82B",
     "A54FF53A5F1D36F1",
     "510E527FADE682D1",
     "9B05688C2B3E6C1F",
     "1F83D9ABFB41BD6B",
     "5BE0CD19137E2179"]

def input_formatting(input_mess):
    # for c in input_mess:
    #     print(str(bin(ord(c))[2:].zfill(8)))

    input_mess_ascii_bin = ''.join(str(bin(ord(c))[2:].zfill(8)) for c in input_mess)
    # print(input_mess_ascii_bin)

    input_mess_ascii_hex = ''.join(str(hex(ord(c))[2:]) for c in input_mess)
    # print(input_mess_ascii_hex)

    len_of_mess = hex(len(input_mess_ascii_bin))[2:].zfill(32)
    # print(len_of_mess)

    num_block = int((len(input_mess_ascii_hex)+len(len_of_mess))/256) + 1

    print(num_block)

    mess = input_mess_ascii_hex + "80" + len_of_mess.zfill(256*num_block - 2 - len(input_mess_ascii_hex))

    print(len(mess))
    print(mess)

    return mess, num_block

def hash_buffer_initialization(mess, numblock):
    block_mess = [mess[i*256:i*256+256] for i in range(numblock)]
    print(block_mess)
    # for c in block_mess:
    #     print(c)

input_mess = input()
mes, nu = input_formatting(input_mess)
hash_buffer_initialization(mes, nu)