
arr = [1]

n = 3
while n <= 1001:
    for i in range(4):
        arr.append(arr[-1] + n-1)
    n += 2

print(arr)
print(sum(arr))