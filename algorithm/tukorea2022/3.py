m1, m2, n = map(int, input().split())

com1 = input()
com2 = input()
encoded = input()

decoded = " "

for i, v in enumerate(encoded):
    if v != decoded[-1]:
        decoded += v

if decoded.count(com1):
    print('YES')
else:
    print('NO')
    
if decoded.count(com2):
    print('YES')
else:
    print('NO')