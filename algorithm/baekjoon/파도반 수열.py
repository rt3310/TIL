t = int(input())

cases = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

tests = []
for i in range(t):
    tests.append(int(input()))

n = max(tests)
for j in range(11, n+1):
    cases.append(cases[j-1] + cases[j-5])

for i in tests:
    print(cases[i])