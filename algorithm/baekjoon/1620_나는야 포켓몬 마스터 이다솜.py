n, m = list(map(int, input().split()))

pocketmons = {}
for i in range(1, n+1):
    name = input()
    pocketmons[name] = str(i)
    pocketmons[str(i)] = name
    
for _ in range(m):
    print(pocketmons[input()])