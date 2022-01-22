import re

def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9-_.]", '', new_id)
    new_id = re.sub("[.]{2,}", '.', new_id)
    new_id = re.sub("^[.]", '', new_id)
    new_id = re.sub("[.]$", '', new_id)
    print(new_id)
    if len(new_id) == 0:
        new_id = 'a'
    new_id = new_id[:15]
    
    if len(new_id) < 3:
        new_id += (new_id[len(new_id) - 1] * (3 - len(new_id)))
    
    new_id = re.sub("^[.]", '', new_id)
    new_id = re.sub("[.]$", '', new_id)
    
    answer = new_id
    
    return answer