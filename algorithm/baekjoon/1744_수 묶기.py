n = int(input())

array = []
zero = 0
minus = []
for _ in range(n):
    number = int(input())
    if number > 0:
        array.append(number)
    elif number == 0:
        zero += 1
    else:
        minus.append(-number)

array.sort(reverse=True)
minus.sort(reverse=True)

total = 0
tmp = None
for i in range(len(array)):
    if tmp is None:
        tmp = array[i]
        if i == len(array) - 1:
            total += tmp
    else:
        if array[i] > 1:
            total += tmp * array[i]
        else:
            total += tmp + array[i]
        tmp = None
    array[i] = 0

tmp = None
for i in range(len(minus)):
    if tmp is None:
        tmp = minus[i]
        if i == len(minus) - 1 and zero == 0:
            total -= tmp
    else:
        total += tmp * minus[i]
        tmp = None
    minus[i] = 0

print(total)
