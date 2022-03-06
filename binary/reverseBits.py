def reverseBits(n):
    res = 0
    for i in range(32):
        r = (n & 1)
        res = (res << 1) + r
        n = n >> 1
    return res


n = 0b00000010100101000001111010011100
print(reverseBits(n))
