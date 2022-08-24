import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sum(numbers[a-1:b]))
    
# 풀이중