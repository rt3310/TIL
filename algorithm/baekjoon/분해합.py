def check(a, b, c):
    if c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')

while True:
    a, b, c = list(map(int, input().split()))
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if c >= a and c >= b:
        check(a, b, c)
    elif b >= a and b >= c:
        check(a, c, b)
    else:
        check(b, c, a)