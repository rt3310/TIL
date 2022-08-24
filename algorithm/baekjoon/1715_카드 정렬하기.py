import heapq

n = int(input())

cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

total = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    compare = a + b
    heapq.heappush(cards, compare)
    total += compare

print(total)