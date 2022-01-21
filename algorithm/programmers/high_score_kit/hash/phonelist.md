# 전화번호 목록


## 문제

### 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

### 입력
- 전화번호를 담은 배열 phone_book

### 출력
- 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true

### 제한사항
- phone_book의 길이는 1 이상 1,000,000 이하
    - 각 전화번호의 길이는 1 이상 20 이하
    - 같은 전화번호가 중복해서 들어있지 않다.


## 해결방안
- 각 문자열의 길이를 저장하고 각 문자열마다 해당 길이로 잘랐을 때 값이 존재하는 지 확인하였다.
    - 해당 문자열보다 긴 길이로 슬라이싱할 경우 중복이 발생하기 때문에 continue하였다.
    - ['1', '22', '23']의 경우 길이가 1인 문자열이 있어서 '22'와 '23' 모두 1로 슬라이싱하면 '2' 로 동일해지기 때문에, 미리 각 문자열을 0으로 초기화시키고 존재하는 문자들만 슬라이싱 되도록 처리하였다.


## 코드 분석
```python3
def solution(phone_book):
    answer = True
    book = {}
    
    lengths = set()
    for i in range(len(phone_book)): # 집합에 중복없이 할당
        lengths.add(len(phone_book[i]))
    lengths = list(lengths)
    
    for i in range(len(phone_book)): # 해시에 존재하는 key의 value값 초기화
        book[phone_book[i]] = 0
    
    for i in range(len(phone_book)):
        for j in lengths:
            if j > len(phone_book[i]): # key 문자열의 길이보다 긴 값의 경우 지나감
                continue
            if book.get(phone_book[i][:j]) != None: # 해시에 값이 존재할 시
                book[phone_book[i][:j]] += 1
                
    if max(book.values()) != 1: # 2번 이상 나온 값이 있을 경우
        answer = False
    return answer
```

- 작성한 코드의 탐색의 경우 O(n^2)의 시간복잡도를 가진다.
