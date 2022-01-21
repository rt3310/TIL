def solution(numbers, hand):
    answer = ''
    
    left = 10
    right = 12
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left = i
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            right = i
            answer += 'R'
        else:
            if i == 0:
                i = 11
            if left == 0:
                left = 11
            if right == 0:
                right = 11
            left_sub = abs(i-left)
            right_sub = abs(i-right)
            left_distance = (left_sub // 3) + (left_sub % 3)
            right_distance = (right_sub // 3) + (right_sub % 3)
            if left_distance < right_distance:
                left = i
                answer += 'L'
            elif right_distance < left_distance:
                right = i
                answer += 'R'
            else:
                if hand == "left":
                    left = i
                    answer += 'L'
                else:
                    right = i
                    answer += 'R'
    return answer