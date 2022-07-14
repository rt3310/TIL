from collections import deque
import time

# n = int(input())

# queue = deque()
# queue.appendleft([n, 0])

# start = time.time()
# store = {}
# while len(queue) != 0:
#     number, count = queue.pop()

#     if number == 1:
#         print(count)
#         break
    
#     if number % 3 == 0:
#         if number // 3 == 1:
#             print(count + 1)
#             break
#         queue.appendleft([number // 3, count + 1])
#         store[number // 3] = count + 1
#     if number % 2 == 0:
#         if number // 2 == 1:
#             print(count + 1)
#             break
#         queue.appendleft([number // 2, count + 1])
#         store[number // 2] = count + 1
#     if number - 1 == 1:
#         print(count + 1)
#         break
#     queue.appendleft([number - 1, count + 1])
#     store[number - 1] = count + 1

# print("time: ", time.time() - start)

n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
        
print(dp[n])