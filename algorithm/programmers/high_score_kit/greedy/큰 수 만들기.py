def solution(number, k):

    length = len(number) - k
    answer = number[0]
    number = number[1:]

    for i, v in enumerate(number):
        while k > 0 and len(answer) > 0:
            if answer[-1] < v:
                answer = answer[:-1]
                k -= 1
            else:
                answer += v
                break
        else:
            answer += number[i]
        if k == 0:
            answer += number[i+1:]
            break

    return answer[:length]