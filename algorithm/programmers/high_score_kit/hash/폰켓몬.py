def solution(nums):
    answer = 0

    d = {}

    for i in nums:
        d[i] = d.get(i, 0) + 1

    answer = min(len(nums)//2, len(d.keys()))
    return answer
