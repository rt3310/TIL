answer = 0


def solution(numbers, target):

    def search(total, v, sign):
        global answer

        if v == len(numbers):
            return

        if sign:
            total += numbers[v]
        else:
            total -= numbers[v]

        if total == target and v == len(numbers) - 1:
            answer += 1

        search(total, v+1, True)
        search(total, v+1, False)

    search(0, 0, True)
    search(0, 0, False)

    return answer
