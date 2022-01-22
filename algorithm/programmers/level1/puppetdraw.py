def solution(board, moves):
    answer = 0
    bucket = []
    n = len(board)

    peek = 0
    for i in moves:
        for j in range(n):
            if board[j][i - 1] == 0:
                continue

            if peek == board[j][i - 1]:
                answer += 1
                bucket.pop(len(bucket) - 1)
                if len(bucket) > 0:
                    peek = bucket[len(bucket) - 1]   
            else:
                peek = board[j][i - 1]
                bucket.append(peek)

            board[j][i - 1] = 0
            break
            
    answer *= 2
    return answer