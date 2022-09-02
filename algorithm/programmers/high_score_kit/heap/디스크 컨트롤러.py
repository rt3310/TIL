from heapq import heappush, heappop


def solution(jobs):
    answer = 0

    jobs.sort(reverse=True)
    length = len(jobs)

    time = 0
    jobq = []
    working_time = 0
    while jobq or jobs:
        while jobs:
            if jobs[-1][0] <= time:
                job = jobs.pop()
                heappush(jobq, [job[1], job[0]])
            else:
                break

        if jobq and working_time <= 0:
            job = heappop(jobq)
            working_time = job[0]
            answer += (time-job[1]) + working_time

        working_time -= 1
        time += 1

    return answer // length
