from collections import deque
n = int(input())

stairs = deque()

for _ in range(n):
    stairs.appendleft(int(input()))

dp = list()
answer = 0
if n < 3:
    answer = sum(stairs)
else:
    dp = [stairs[0], stairs[0] + stairs[1], stairs[0] + stairs[2]]
    
    for i in range(3, len(stairs)):
        dp.append(max(stairs[i] + dp[-2], stairs[i-1] + stairs[i] + dp[-3]))
        
    answer = max(dp[-1], dp[-2])

print(answer)