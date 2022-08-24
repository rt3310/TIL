n, m = list(map(int, input().split()))

hashmap = {}
for _ in range(n):
    addr, pw = input().split()
    hashmap[addr] = pw

for _ in range(m):
    print(hashmap[input()])