n, k = list(map(int, input().split()))

children = list(map(int, input().split()))
max_diff = children[-1] - children[0]
avr_diff = max_diff // k

init = children[0]
cost = 0
for i in range(len(children) - 1):
    if children[i+1] - init > avr_diff:
        cost += (children[i] - init)
        init = children[i+1]

print(cost)


