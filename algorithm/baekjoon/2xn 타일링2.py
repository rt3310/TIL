n = int(input())

cases = [0, 1, 3]

for i in range(3, n+1):
    cases.append((cases[i-1] + (cases[i-2] * 2)) % 10007)

print(cases[n])