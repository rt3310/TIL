import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    tmp = []
    for i in input().strip():
        tmp.append(i)
    arr.append(tmp)

def search(arr, start):
    q = deque([start])
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    arr[start[0]][start[1]] = '2'
    
    count = 1
    while q:
        cur = q.popleft()
        
        for c, r in direct:
            if cur[0]+r < 0 or cur[0]+r >= n or cur[1]+c < 0 or cur[1]+c >= n:
                continue
            if arr[cur[0]+r][cur[1]+c] == '1':
                arr[cur[0]+r][cur[1]+c] = '2'
                count += 1
                q.append([cur[0]+r, cur[1]+c])
    return count

result = []
for i, iv in enumerate(arr):
    for j, jv in enumerate(iv):
        if jv == '1':
            result.append(search(arr, [i, j]))

print(len(result))
for i in sorted(result):
    print(i)