n, k = list(map(int, input().split()))

cases = [[1]]
tmp = [[1 for _ in range(n+1)] for _ in range(k+1)]
cases.extend(tmp)

for i in range(2, k):
    for j in range(n+1):
        cases[i][j] = sum(cases[i-1][:j+1])

print(sum(cases[k-1]) % 1000000000)