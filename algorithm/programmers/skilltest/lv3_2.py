from collections import defaultdict

def solution(genres, plays):
    answer = []

    genres_count = defaultdict(int)
    genres_plays = defaultdict(list)
    for i, v in enumerate(genres):
        genres_count[v] += plays[i]
        genres_plays[v].append([plays[i], -i])
        
    print('?:', genres_count)
    genres_count = sorted(genres_count, key=lambda x: genres_count[x], reverse=True)

    for i in genres_count:
        playlists = genres_plays[i]
        playlists.sort(reverse=True)
        print(playlists)
        for idx, j in enumerate(playlists):
            if idx > 1:
                break
            answer.append(-j[1])

    return answer

print(solution(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5]))