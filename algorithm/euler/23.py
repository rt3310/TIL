def get_divisor_sum(number):
    divisor = []
    for i in range(1, number):
        if number % i == 0:
            divisor.append(i)
    return sum(divisor)

over_list = []
count = 1
for count in range(1, 28123):
    divisor_sum = get_divisor_sum(count)
    if divisor_sum > count:
        over_list.append(count)

possible_list = set()
for i, v in enumerate(over_list):
    for j in range(i, len(over_list)):
        if v + over_list[j] >= 28123:
            break
        possible_list.add(v + over_list[j])

impossible_list = set([i for i in range(1, 28123)]) - possible_list

print(sum(impossible_list))