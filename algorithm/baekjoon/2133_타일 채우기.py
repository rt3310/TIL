n = int(input())

if n % 2 == 1:
    print(0)
else:
    dp = [0] * (n//2+1)

    dp[1] = 3
    for i in range(2, n//2+1):
        dp[i] = (dp[i-1] * 3)+((i-1)*2)

    print(dp[n//2])