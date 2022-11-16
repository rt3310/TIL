from functools import cache

pens = [1, 2, 5, 10, 20, 50]
dp = [1, 2]

for i in range(2, 201):
    dp.append(1 + dp[i-2])

print(dp)