from collections import deque

n = int(input())
pair = int(input())

graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
for _ in range(pair):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def search(init):
    q = deque([init])
    while q:
        com = q.popleft()
        for i in graph[com]:
            if visit[i] == False:
                q.append(i)
                visit[i] = True
                
search(1)
print(visit.count(True)-1)