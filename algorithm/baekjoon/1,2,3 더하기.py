T = int(input())

cases = [0] * 12

cases[1] = 1
cases[2] = 2
cases[3] = 4

for j in range(4, 12):
    cases[j] = cases[j-1] + cases[j-2] + cases[j-3]

for i in range(T):
    n = int(input())
    print(cases[n])