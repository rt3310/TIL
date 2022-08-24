n = int(input())

s = 0
for _ in range(n):
    string = input() + " 0"
    command, num = string.split()[0], string.split()[1]
    num = int(num)
    
    if command == 'add':
        s = s | (1 << num)
    elif command == 'remove':
        s = s & ~(1 << num)
    elif command == 'check':
        t = s & (1 << num)
        if t != 0:
            t = 1
        print(t)
    elif command == 'toggle':
        s = s ^ (1 << num)
    elif command == 'all':
        s = (1 << 20)
    else:
        s = 0