def seek_share(a, b):
    for i, iv in enumerate(a):
        for j, jv in enumerate(b):
            if iv == jv:
                return j, i

a, b = input().split()

row = len(b)
col = len(a)

a_idx, b_idx = seek_share(a, b)

for i in range(row):
    for j in range(col):
        if i == a_idx:
            print(a[j], end='')
            continue
        if j == b_idx:
            print(b[i], end='')
            continue
        print('.', end='')
    print()