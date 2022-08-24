from collections import deque

m, n = list(map(int, input().split()))

direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
box = []
for i in range(n):
    box.append(list(map(int, input().split())))

tomatos = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomatos.append([i, j])

def search(initlist):
    q = deque(initlist)
    while q:
        curx, cury = q.popleft()
        for i in direct:
            seekx = curx + i[0]
            seeky = cury + i[1]
            if seekx >= 0 and seekx < n and seeky >= 0 and seeky < m:
                if box[seekx][seeky] == 0:
                    q.append([seekx, seeky])
                    box[seekx][seeky] = box[curx][cury] + 1

search(tomatos)

status = 1
for i in box:
    for j in i:
        if j == 0:
            status = 0
            break
        if j > status:
            status = j
    if status == 0:
        break

print(status-1)