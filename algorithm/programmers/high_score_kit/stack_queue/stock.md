# 주식가격


## 문제

### 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

### 입력
- 초 단위로 기록된 주식가격이 담긴 배열 prices

### 출력
- 가격이 떨어지지 않은 시간(초)

### 제한사항
- prices의 각 가격은 1 이상 10,000 이하인 자연수
- prices의 길이는 2 이상 100,000 이하


## 해결방안
- 이중 반복문을 이용한 선형탐색으로 주식가격의 하락 여부를 측정하였다.


## 코드 분석
```python3
def solution(prices):
    answer = []
    
    for i in range(len(prices)): # 기준 가격
        breaked = 0
        time = 0
        for j in range(i + 1, len(prices)): # 떨어진 상황 체크
            time += 1
            if prices[j] < prices[i]:
                answer.append(time)
                breaked = 1
                break
        if breaked == 0: # 떨어지지 않았을 시
            answer.append(time)
    return answer
```
- 작성한 코드는 O(n^2)의 시간복잡도를 가진다.


## 보충
- 더 나은 방법이 있을 것 같다. 추후에 탐색 알고리즘에 대해 더 알아보고 보충할 예정
