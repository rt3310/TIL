n = int(input())

seq = list(map(int, input().split()))

dp = [[0] * n, [0] * n]

dp[0][0] = seq[0]
dp[1][0] = 1

for i in range(1, n):
    if seq[i] > seq[i-1]:
        dp[0][i] = dp[0][i-1] + 1
        dp[1][i] = dp[1][i-1]
        
    else:
        if seq[i] >= dp[1][i-1]:
            dp[0][i] = dp[0][i-1]
            dp[1][i] = dp[1][i-1]
            dp[2][i] = dp[2][i-1]
        else:
            dp[0][i] = 1
            dp[1][i] = seq[i]
            dp[2][i] = dp[2][i-1]            

print(dp)