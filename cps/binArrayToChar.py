import binascii


def vbin2char(bin):
    # print("Da")
    # print(bin)
    str1 = ''.join(str(e) for e in bin)
    # print(str1)
    n = int('0b' + str1, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
