def solution(sizes):
    answer = 0

    long = 0
    short = 0
    for i in sizes:
        longer = max(i)
        shorter = min(i)
        long = max(long, longer)
        short = max(short, shorter)

    answer = long * short
    return answer
