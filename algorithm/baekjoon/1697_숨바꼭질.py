from collections import deque

n, k = map(int, input().split())

visit = [-1] * 100001

def search(n):
    q = deque([n])
    
    visit[n] = 0
    while q:
        pos = q.popleft()
        if pos == k:
            print(visit[pos])
            return
        if pos * 2 <= 100000 and visit[pos * 2] == -1:
            q.append(pos * 2)
            visit[pos * 2] = visit[pos] + 1
        if pos - 1 >= 0 and visit[pos - 1] == -1:
            q.append(pos - 1)
            visit[pos - 1] = visit[pos] + 1
        if pos + 1 <= 100000 and visit[pos + 1] == -1:
            q.append(pos + 1)
            visit[pos + 1] = visit[pos] + 1
        
search(n)