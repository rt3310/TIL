from collections import deque


def solution(people, limit):
    answer = 0

    deq_people = deque(sorted(people))
    while len(deq_people) > 0:
        total = 0
        total += deq_people.pop()
        while len(deq_people) > 0 and deq_people[0] <= (limit - total):
            total += deq_people.popleft()
        total = 0
        answer += 1

    return answer
