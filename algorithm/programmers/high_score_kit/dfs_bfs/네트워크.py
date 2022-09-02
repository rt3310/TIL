def solution(n, computers):
    answer = 0

    visited = [False] * n

    def search(v, visited):
        if visited[v] == True:
            return False
        visited[v] = True

        for i in range(len(computers[v])):
            if computers[v][i] == 1 and visited[i] == False:
                search(i, visited)

        return True

    for i in range(len(computers)):
        if search(i, visited):
            answer += 1
    return answer
