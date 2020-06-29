def get_nth_bit_from_char(n, c):
    nth_bit = (2 ** n) & ord(c)
    return nth_bit >> n # shift the bit right to the ones place


def encode(s):
    
    s = s.ljust(4, '\0') # pad input with null, which is ascii 0
    a = 0
    
    for j in range(7, -1, -2):
        a = a << 8
        for i in range(3, -1, -1): # 3, 2, 1, 0
            a = a | (get_nth_bit_from_char(j, s[i]) << (4 + i))
        
        for i in range(3, -1, -1): # 3, 2, 1, 0
            a = a | (get_nth_bit_from_char(j - 1, s[i]) << i)
    
    return a
