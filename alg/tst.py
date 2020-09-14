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

    print(mess)

    return mess, num_block

def hash_buffer_initialization(mess, numblock):
    block_mess = [].append(mess[:])

input_mess = input()

input_formatting(input_mess)