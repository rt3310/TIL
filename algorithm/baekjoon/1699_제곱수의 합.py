import sys, math

input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n+1)]

for i in range(1, n+1):
    count = 1
    while count**2 <= i:
        dp[i] = min(dp[i], dp[i-(count**2)] + 1)
        count += 1

print(dp[n])