# 베스트앨범


## 문제

### 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

### 입력
- 노래의 장르를 나타내는 문자열 배열 genres
- 노래별 재생 횟수를 나타내는 정수 배열 plays

### 출력
- 기준의 순서에 따른 베스트 앨범에 들어갈 노래의 고유 번호

### 제한사항
- genres[i]는 고유번호가 i인 노래의 장르이다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수이다.
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하이다.
- 장르 종류는 100개 미만
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택
- 모든 장르는 재생된 횟수가 다르다.

## 해결방안
- 딕셔너리에 총합과 재생 수 리스트를 저장 후, 리스트에 [장르 별 총합, 재생 수, 고유변호]형식으로 할당하여 정렬하였다.
    - 장르 별 총합과 재생 수는 내림차순으로 정렬해야하지만 고유번호는 오름차순으로 정렬해야 되기 때문에 음수로 먼저 할당하여 정렬한 다음 -1 을 곱하여 출력되도록 하였다.


## 코드 분석
```python3
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
```
- 작성한 코드의 탐색은 O(n)의 시간복잡도를 가진다.


## 보충
- list의 sort()에 의존하는 것 같아서 정렬 알고리즘 학습 후 다시 짜봐야 될거같다.
- 참고로 list에 내장되어 있는 sort()는 팀소트 알고리즘으로 O(nlogn)의 시간복잡도를 가진다. 성능이 좋다.