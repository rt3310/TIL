from copy import deepcopy


def solution(id_list, report, k):
    answer = []
    
    report_member = {}
    for i in id_list:
        report_member[i] = []
    
    report_count = {}    
    for i in id_list:
        report_count[i] = 0
        
    stoped_id = deepcopy(report_count)
    
    for i in report:
        reporter, respondent = i.split(' ')
        if report_member[reporter].count(respondent) == 0:
            report_member[reporter].append(respondent)
    
    for i in report_member.values():
        for j in id_list:
            report_count[j] += i.count(j)
    
    for i in id_list:
        for j in report_member[i]:
            if report_count[j] >= k:
                stoped_id[i] += 1
    
    answer = list(stoped_id.values())
    return answer