def solution(s):
    answer = True

    stack = []

    for i in s:
        if i == ")":
            if len(stack) == 0 or stack[-1] != "(":
                answer = False
                break
            else:
                stack.pop()
        else:
            stack.append(i)
    else:
        if len(stack) == 0:
            answer = True
        else:
            answer = False

    return answer
