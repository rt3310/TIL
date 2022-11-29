import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    tmp = []
    for i in input().strip():
        tmp.append(int(i))
    arr.append(tmp)

def search(arr, cur):
    q = deque([cur])
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    arr[cur[0]][cur[1]] = 2
    
    while q:
        cur = q.popleft()
        
        for r, c in direct:
            if cur[0]+r < 0 or cur[0]+r >= n or cur[1]+c < 0 or cur[1]+c >= m:
                continue
            if arr[cur[0]+r][cur[1]+c] == 1:
                arr[cur[0]+r][cur[1]+c] = arr[cur[0]][cur[1]] + 1
                q.append([cur[0]+r, cur[1]+c])

search(arr, [0, 0])
print(arr[n-1][m-1]-1)