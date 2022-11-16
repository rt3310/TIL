b, n, m = map(int, input().split())

narr = list(map(int, input().split()))[::-1]
marr = list(map(int, input().split()))[::-1]

n10 = narr[0]
m10 = marr[0]
for i in range(1, n):
    n10 += narr[i] * (b**i)
    
for i in range(1, m):
    m10 += marr[i] * (b**i)

result = []
mul = n10 * m10
while mul > 0:
    result.append(mul % b)
    mul //= b
result = result[::-1]

print(len(result))
print(*result)