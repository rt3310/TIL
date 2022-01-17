# H-Index


## 문제

### 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 `n`편 중, `h`번 이상 인용된 논문이 `h`편 이상이고 나머지 논문이 h번 이하 인용되었다면 `h`의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

### 입력
- 논문의 인용 횟수를 담은 배열 citations

### 출력
- H-Index

### 제한사항
- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하
- 논문별 인용 횟수는 0회 이상 10,000회 이하


## 해결방안
- 처음엔 citations를 오름차순으로 정렬하여 에 있는 요소를 기준으로 탐색하였다. 그런데 많은 케이스에서 실패가 나왔다. 인용횟수의 최솟값이 h-index 값일 거라는 착각을 한것이다.
    - 예를 들어, [5, 5, 5, 5] 에서는 h-index 값이 4이지만 요소 기준으로 탐색하니 5는 h-index가 5가 될 수 없어 0으로 출력됐다.
    - 위 오류를 수정하기 위해 내림차순으로 정렬 후 index값을 기준으로 해당 요소 값이 index 보다 큰 값인지 검사하였다.


## 코드 분석
```python3
def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)

    print(citations)
    for i, v in enumerate(citations):
        if v >= i + 1:
            answer = i + 1

    return answer
```
- 작성한 코드의 탐색 부분은 O(n)의 시간복잡도를 가진다.
