def solution(k, dungeons):
    answer = 0

    dungeons = sorted(
        list(map(lambda x: [x[0], -x[1]], dungeons)), reverse=True)

    visited = [False] * len(dungeons)

    def search(dungeons, count, fatigue, idx, visited):
        global answer
        count += 1
        fatigue += dungeons[idx][1]
        visited[idx] = True

        max_cnt = count
        for i, v in enumerate(dungeons):
            if fatigue >= v[0] and visited[i] == False:
                print(count)
                max_cnt = max(max_cnt, search(
                    dungeons, count, fatigue, i, visited[:]))
        return max_cnt

    answer = 0
    for i, v in enumerate(dungeons):
        answer = max(answer, search(dungeons, 0, k, i, visited[:]))

    return answer
