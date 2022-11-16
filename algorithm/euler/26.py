def reptend(d):
    remains, quot = [], ""
    remain = 1
    print('d:', d)
    while remain > 0:
        remains.append(remain)
        quotient, remain = divmod(remain*10, d)
        quot = quot + str(quotient)
        print('remains:', remains)
        print('quot:', quot)
        if remain in remains:
            pos = remains.index(remain)
            return quot[pos:]
    return ""

for i in range(6, 8):
    print(reptend(i))