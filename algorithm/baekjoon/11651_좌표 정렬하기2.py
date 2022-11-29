import sys

input = sys.stdin.readline

n = int(input())

dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append([x, y])
    
dots.sort(key=lambda x: (x[1], x[0]))

for i in dots:
    print(*i)