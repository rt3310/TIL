def solution(name):
    answer = 0
    name_list = []

    for i in range(len(name)):
        name_list.append(
            (91 - ord(name[i])) if (ord(name[i]) - 65) > 13 else (ord(name[i]) - 65))

    change_cnt = sum(name_list)

    if change_cnt == 0:
        return 0

    name_list_len = len(name_list)
    a_count = 0
    max_a = 0
    start_idx = 0
    max_start_idx = 0
    max_end_idx = 0
    for i in range(name_list_len * 2):
        if name_list[i % name_list_len] == 0:
            if name_list[(i - 1) % name_list_len] != 0:
                start_idx = i % name_list_len
            a_count += 1
        else:
            if a_count > max_a:
                max_start_idx = start_idx
                max_end_idx = (i - 1) % name_list_len
                max_a = a_count
            a_count = 0

    if max_a == 0:
        return name_list_len - 1 + change_cnt

    length = 0
    start_idx = 0
    end_idx = 0
    if max_start_idx > max_end_idx:
        start_idx = max_end_idx + 1
        end_idx = max_start_idx - 1
        length = end_idx - start_idx + 1
        if start_idx < name_list_len - end_idx:  # 3 7 3
            answer = start_idx + length - 1 + change_cnt
        else:
            answer = (name_list_len - end_idx) - 1 + length + change_cnt
    else:
        start_idx = max_end_idx + 1
        end_idx = max_start_idx - 1
        length = (name_list_len - start_idx) + end_idx + 1
        if end_idx < name_list_len - start_idx:
            if end_idx < start_idx - end_idx - 1:
                answer = end_idx * 2 + (name_list_len - start_idx) + change_cnt
            else:
                answer = name_list_len - 1 + change_cnt
        else:
            if name_list_len - start_idx - 1 < start_idx - end_idx - 1:
                answer = (name_list_len - start_idx) * 2 + end_idx + change_cnt
            else:
                answer = name_list_len - 1 + change_cnt

    return answer
