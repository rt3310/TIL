from itertools import permutations


def solution(numbers):
    answer = 0

    number_permu = []
    for i in range(1, len(numbers)+1):
        number_permu.extend(list(permutations(numbers, i)))
    # 짝수x, 5x, 자릿수 합 3의 배수x

    number_combi = {}
    for i in number_permu:
        num = int(''.join(i))
        if (num > 2 and num % 2 != 0) or num == 2:
            number_combi[num] = 1
    number_combi = list(number_combi.keys())

    for i in number_combi:
        is_prime = False
        for j in range(3, i // 2 + 1, 2):
            if i % j == 0:
                is_prime = True
                break
        if is_prime == False:
            answer += 1
    return answer
