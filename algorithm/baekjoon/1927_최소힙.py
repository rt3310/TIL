import heapq, sys

n = int(sys.stdin.readline())

heap = []
length = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if length == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
            length -= 1
    else:
        heapq.heappush(heap, num)
        length += 1