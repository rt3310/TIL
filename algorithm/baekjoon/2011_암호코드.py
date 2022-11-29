import sys

input = sys.stdin.readline

number = input().strip()

dp1 = [0] * len(number)
dp2 = [0] * len(number)

if len(number) > 0 and int(number[0]) > 0:
    dp1[0] = 1
if len(number) > 1 and int(number[1]) > 0:
    dp1[1] = 1
if 9 < int(number[0:2]) < 27:
    dp2[1] = 1

if dp1[0] == 0:
    print(0)
else:
    for i in range(2, len(number)):
        if int(number[i-1:i+1]) > 9 and int(number[i-1:i+1]) < 27:
            dp2[i] = (dp1[i-2]+dp2[i-2])
        
        if int(number[i]) > 0:
            dp1[i] = (dp1[i-1]+dp2[i-1])
            
    print((dp1[-1] + dp2[-1]) % 1000000)