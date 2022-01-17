from audioop import reverse
from operator import ge


def solution(genres, plays):
    answer = []
    
    total = {}
    by_genre = {}
    for i in range(len(genres)):
        total[genres[i]] = 0
        by_genre[genres[i]] = []
    
    for i in range(len(genres)):
        total[genres[i]] += plays[i]
        by_genre[genres[i]].append(plays[i])
    
    sorted_total = sorted(total.items(), reverse=True)
    
    sorted_plays = []
    for i in range(len(by_genre)):
        tmp = sorted(by_genre[sorted_total[i][0]], reverse=True)
        play = [None, None, None]
        play[0], play[1], play[2] = sorted_total[i][0], tmp[0], tmp[1]
        sorted_plays.append(play)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres=genres, plays=plays))

print(range(1000000))