def solution(clothes):
    answer = 1
    
    category = {}
    cloth_count = [] # {옷 종류: 개수}
    
    for i in range(len(clothes)): # 해시에 옷 종류별로 개수 정리
        if category.get(clothes[i][1]) == None:
            category[clothes[i][1]] = 1
        else:
            category[clothes[i][1]] += 1
    
    cloth_count = list(category.values()) # value값들을 list로 변환
    for i in range(len(cloth_count)): # 경우의 수 계산
        answer *= (cloth_count[i] + 1) # 안 입는 경우의 수 포함
    
    answer -= 1 # 아예 안입는 경우 제외
    
    return answer