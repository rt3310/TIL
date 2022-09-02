r, c = map(int, input().split())

land = []
if r % 2 == 1:
    for i in range(r):
        if i % 2 == 0:
            print('R' * (c-1), end='')
        else:
            print('L' * (c-1), end='')
        if i == r-1:
            break
        print('D', end='')
elif c % 2 == 1:
    for i in range(c):
        if i % 2 == 0:
            print('D' * (r-1), end='')
        else:
            print('U' * (r-1), end='')
        if i == c-1:
            break
        print('R', end='')    