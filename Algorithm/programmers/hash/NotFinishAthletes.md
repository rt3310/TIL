# 완주하지 못한 선수


## 문제

### 입력
- 마라톤에 참여한 선수들의 이름이 담긴 배열 paricipant
- 완주한 선수들의 이름이 담긴 배열 completion

### 출력
- 완주하지 못한 선수의 이름

### 제한사항
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하
- completion의 길이는 participant의 길이보다 1 작음
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있음
- 참가자 중에 동명이인이 있을 수 있음


## 해결방안
- 여기서 문제가 되는 사항은 동명이인이 존재한다는 것이였다.
    - 동명이인을 처리하기위한 해결방안으로 {완주자:동명이인 인원 수} 형태로 해시값을 입력하였다.
    - 위에 따라, 참가자를 탐색하여 해시에 존재하지 않거나 value값이 0이면 완주하지 못한 것으로 볼 수 있다.


## 코드 분석
```python3
def solution(participant, completion):
    answer = ''
    comple = {} # {완주자:동명이인 인원 수}

    for i in range(len(completion)):
        if comple.get(completion[i]) == None: # 완주 명단 해시에 없으면
            comple[completion[i]] = 1 # 해시 추가
        else:
            comple[completion[i]] += 1 # value값 증가

    for i in range(len(participant)):
        if comple.get(participant[i]) == None or comple.get(participant[i]) == 0: # 완주 명단에 없으면
            answer = participant[i]
            break
        else: # 동명이인이 있을 시
            comple[participant[i]] -= 1 # value값 감소

    return answer
```
- 작성한 코드의 해시 값 입력, 탐색 모두 O(n)의 시간복잡도를 가진다.
