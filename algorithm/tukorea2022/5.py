from collections import deque

start = []
table = []
for i in range(10):
    tmp = []
    for j, v in enumerate(input()):
        tmp.append(v)
        if v == 'B':
            start = [i, j]
    table.append(tmp)

def search(table, start):
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    q = deque([start])
    
    while True:
        e = q.popleft()
        
        for i in direct:
            if e[0] + i[0] < 0 or e[0] + i[0] > 9:
                continue
            if e[1] + i[1] < 0 or e[1] + i[1] > 9:
                continue
            
            if table[e[0]+i[0]][e[1]+i[1]] == 'L':
                return e[2]
            
            if table[e[0]+i[0]][e[1]+i[1]] == '.':
                table[e[0]+i[0]][e[1]+i[1]] = 'C'
                q.append([e[0]+i[0], e[1]+i[1], e[2]+1])
    
start.append(0)
print(search(table, start))