n = int(input())

wines = []

dp = [0] * n
for i in range(n):
    wines.append(int(input()))

dp[0] = wines[0]
if n > 1:
    dp[1] = wines[0] + wines[1]
if n > 2:
    dp[2] = max(wines[1] + wines[2], wines[0] + wines[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + wines[i], dp[i-3] + wines[i] + wines[i-1])

print(max(dp))