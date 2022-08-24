from collections import defaultdict

names = defaultdict(int)
n, m = list(map(int, input().split()))

for _ in range(n):
    names[input()] += 1

for _ in range(m):
    names[input()] += 1
        
names = sorted(list(filter(lambda x: names[x] == 2, names)))
print(len(names))
for i in names:
    print(i)