from numpy.ma import logical_xor


def syndrome(looper, data, check):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # wektor    zawierający   wynikowy   syndrom


    chunk = (data[looper:looper + 26])
    count =0

    if len(chunk)==26:
        # 26 bit vector rds
        for bit_check in range(0, 26):  # pętlamnożnącay

            if chunk[bit_check]:
                count = count + 1
                result = logical_xor(result, check[bit_check])
    # y*h, sekwencja 26 bitow im macierz parzystosci

    return result





