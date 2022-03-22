from itertools import count


def solution(n, lost, reserve):
    answer = 0

    students = [0 if lost.count(i) else 1 for i in range(n + 2)]
    students[0] = 0
    students[len(students)-1] = 0

    i = 0
    for i in reserve:
        if lost.count(i) == 0:
            students[i] = 2
    
    lost.sort()
    
    for j in lost:
        if students[j - 1] == 2:
            students[j - 1] -= 1
            students[j] = 1
        elif students[j + 1] == 2:
            students[j + 1] -= 1
            students[j] = 1
    
    print(students)
    answer = students.count(1) + students.count(2)
    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))