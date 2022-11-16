def get_divisor_sum(number):
    divisor = []
    for i in range(1, number):
        if number % i == 0:
            divisor.append(i)
    return sum(divisor)

result_set = set()
for a in range(1, 10001):
    b = get_divisor_sum(a)
    c = get_divisor_sum(b)
    if a != c or a == b:
        continue
    result_set.add(a)
    result_set.add(c)
    
print(result_set)
print(sum(result_set))