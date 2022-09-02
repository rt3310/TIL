def solution(m, n, puddles):
    answer = 0

    area = [[0 for _ in range(m)] for _ in range(n)]

    area[0][0] = 1
    for i in puddles:
        area[i[1]-1][i[0]-1] = -1

    for i, v in enumerate(area):
        for j, e in enumerate(v):
            if e == -1:
                continue
            if i != 0 and area[i-1][j] != -1:
                area[i][j] += area[i-1][j]
            if j != 0 and area[i][j-1] != -1:
                area[i][j] += area[i][j-1]

    answer = area[-1][-1] % 1000000007
    return answer
