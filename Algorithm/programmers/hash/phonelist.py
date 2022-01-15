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