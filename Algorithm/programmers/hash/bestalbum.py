from audioop import reverse


def solution(genres, plays):
    answer = []
    
    total = {} # 장르 별 재생 수 총합
    by_genre = {} # 장르 별 재생 수 리스트
    for i in range(len(genres)): # 값 초기화
        total[genres[i]] = 0
        by_genre[genres[i]] = []
    
    for i in range(len(genres)): # 총합 계산 및 재생수 별 index 저장
        total[genres[i]] += plays[i]
        tmp = []
        tmp.append(plays[i])
        tmp.append(-i) # 재생 수가 동일할 경우 낮은 index가 와야하기 때문에 -1로 입력
        by_genre[genres[i]].append(tmp)
    
    # 리스트로 정렬 [[장르 별 총합, 재생 수, index], ...]
    incoded = []
    for k, v in total.items():
        length = 2 if len(by_genre[k]) >= 2 else 1 # 길이가 2 이상이면 2
        sorted_genre = sorted(by_genre[k], reverse=True) # 재생 수 정렬
        for j in range(length): 
            tmp = []
            tmp.append(v)
            tmp.append(sorted_genre[j][0])
            tmp.append(sorted_genre[j][1])
            incoded.append(tmp)
    
    incoded.sort(reverse=True) # 내림차순으로 정렬
    for i in incoded:
        answer.append(i[2] * -1)
        
    return answer