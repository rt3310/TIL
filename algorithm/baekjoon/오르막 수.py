n = int(input())

cases = [0, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
for i in range(2, n+1):

    tmp = []
    for j in range(10):
        tmp.append(sum(cases[i-1][j:]))
    cases.append(tmp)

print(cases[n][0] % 10007)