import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * n
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in graph:
    i.sort()

dfs_result = []
bfs_result = []
def dfs(graph, visited, cur):
    visited[cur-1] = True
    dfs_result.append(cur)
    
    for i in graph[cur]:
        if not visited[i-1]:
            dfs(graph, visited, i)
        

def bfs(graph, visited, start):
    q = deque([start])
    bfs_result.append(start)
    visited[start-1] = True
    
    while q:
        cur = q.popleft()
        
        for i in graph[cur]:
            if not visited[i-1]:
                bfs_result.append(i)
                visited[i-1] = True
                q.append(i)

dfs(graph, visited[:], v)
bfs(graph, visited[:], v)
print(*dfs_result)
print(*bfs_result)