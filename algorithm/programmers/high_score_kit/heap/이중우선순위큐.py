from heapq import heapify, heappop, heappush, nlargest

def solution(operations):
    answer = []

    for i in operations:
        operation, number = i.split()

        if operation == "I":
            heappush(answer, int(number))
        elif operation == "D" and answer:
            if number == "1":
                answer = nlargest(len(answer), answer)[1:]
                heapify(answer)
            else:
                heappop(answer)

    if answer:
        answer = [nlargest(1, answer)[0], heappop(answer)]
    else:
        answer = [0, 0]

    return answer