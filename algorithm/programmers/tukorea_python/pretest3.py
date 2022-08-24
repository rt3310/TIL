def solution(sizes):
    answer = 0

    longer = 0
    shorter = 0
    for i in sizes:
        if i[0] >= i[1]:
            longer = max(longer, i[0])
            shorter = max(shorter, i[1])
        else:
            longer = max(longer, i[1])
            shorter = max(shorter, i[0])

    answer = longer * shorter
    return answer
