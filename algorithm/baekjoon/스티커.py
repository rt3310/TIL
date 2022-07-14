t = int(input())

for i in range(t):
    n = int(input())
    dp = [[0] * (n+1), [0] * (n+1)]
    st_list = list(map(int, input().split()))
    nd_list = list(map(int, input().split()))
    
    dp[0][0] = st_list[0]
    dp[1][0] = nd_list[0]
    
    if n > 1:        
        dp[0][1] = nd_list[0] + st_list[1]
        dp[1][1] = st_list[0] + nd_list[1]
    
    for j in range(2, len(st_list)):
        dp[0][j] = max(dp[1][j-1] + st_list[j], dp[1][j-2] + st_list[j])
        dp[1][j] = max(dp[0][j-1] + nd_list[j], dp[0][j-2] + nd_list[j])
                
    print(max(dp[0][n-1], dp[1][n-1]))