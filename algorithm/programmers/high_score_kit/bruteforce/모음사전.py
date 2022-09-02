def solution(word):
    answer = 0

    alpha_dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    alpha = ['A', 'E', 'I', 'O', 'U']

    compare = ""

    count = 0
    while compare != word:
        if len(compare) < 5:
            compare += alpha[0]
        else:
            while alpha_dict[compare[-1]] == 4:
                compare = compare[:-1]
            compare = compare[:-1] + alpha[alpha_dict[compare[-1]]+1]
        count += 1

    answer = count
    return answer
