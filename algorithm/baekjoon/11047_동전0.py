n, k = list(map(int, input().split()))

coins = [0] * n

for i in range(n):
    coins[-i-1] = int(input())

count = 0
while k > 0:
    for i in coins:
        if i <= k:
            count += k // i
            k %= i
            break
print(count)