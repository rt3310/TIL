def solution(n, lost, reserve):
    answer = 0

    gymsuits = [1] * n

    for i in lost:
        gymsuits[i-1] -= 1

    for i in reserve:
        gymsuits[i-1] += 1

    for i, v in enumerate(gymsuits):
        if v == 0:
            if i > 0 and gymsuits[i-1] > 1:
                gymsuits[i] += 1
                gymsuits[i-1] -= 1
            elif i < n-1 and gymsuits[i+1] > 1:
                gymsuits[i] += 1
                gymsuits[i+1] -= 1

    answer = len(list(filter(lambda x: x > 0, gymsuits)))
    return answer