def vbin2dec(bin):

    str1 = ''.join(str(e) for e in bin)
    n = int('0b'+str1, 2)
    return n

