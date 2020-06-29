def get_nth_bit_from_char(n, c):
    nth_bit = (2 ** n) & c
    return nth_bit >> n # shift the bit right to the ones place

print('[')
for bits in range(0, 4):
    print("\t{")
    for c in range(0, 127): # skip last 8bit char because it is not printable
        if chr(c).isprintable() or c == 0:
            first_byte = (get_nth_bit_from_char(0, c) << bits) + (get_nth_bit_from_char(1, c) << (bits + 4))
            second_byte = ((get_nth_bit_from_char(2, c) << bits) + (get_nth_bit_from_char(3, c) << (bits + 4))) << 8
            third_byte = ((get_nth_bit_from_char(4, c) << bits) + (get_nth_bit_from_char(5, c) << (bits + 4))) << 16
            forth_byte = ((get_nth_bit_from_char(6, c) << bits) + (get_nth_bit_from_char(7, c) << (bits + 4))) << 24
            
            result = first_byte + second_byte + third_byte + forth_byte
            if c == 0: #escape null
                print("\t\t" + "'" + '\\0' + "'" + ': ' + str(result) + ',')
            elif c == 39: # escape single quote
                print("\t\t" + '"' + chr(c) + '"' + ': ' + str(result) + ',')
            elif c == 92: # escape back slash
                print("\t\t" + "'\\" + chr(c) + "'" + ': ' + str(result) + ',')
            elif c != 127:
                print("\t\t" + "'" + chr(c) + "'" + ': ' + str(result) + ',')
            else:
                print("\t\t" + "'" + chr(c) + "'" + ': ' + str(result))
    if bits != 3:
        print("\t},")
    else:
        print("\t}")

print(']')
