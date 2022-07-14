pos = list(map(int, input().split()))

pos[2] -= pos[0]
pos[3] -= pos[1]

print(min(pos))