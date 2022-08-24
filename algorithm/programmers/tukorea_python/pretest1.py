def solution(s):
    answer = True

    p = 0
    y = 0
    for i in s:
        word = i.lower()
        if word == 'p':
            p += 1
        elif word == 'y':
            y += 1

    if p != y:
        answer = False
    return answer
