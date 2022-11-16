def seek_not_duplicated(n):
    n += 1
    while True:
        if n > 987654321:
            return 0
        counts = {'0': 1}
        str_n = str(n)
        for i, v in enumerate(str_n):
            if counts.get(v) is None:
                counts[v] = 1
            else:
                tmp = 10**(len(str_n) - i - 1)
                n = (n // tmp + 1) * tmp
                break
        else:
            return n
        
print(seek_not_duplicated(int(input())))