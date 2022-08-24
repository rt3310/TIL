def solution(s):
    answer = ''

    words = ['zero', 'one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']

    while s:
        if s[0].isdigit():
            answer += s[0]
            s = s[1:]
        else:
            for i, v in enumerate(words):
                if s[:len(v)] == v:
                    answer += str(i)
                    s = s[len(v):]

    return int(answer)