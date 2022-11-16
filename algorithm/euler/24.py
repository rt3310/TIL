word = [str(i) for i in range(10)]
visited = [False] * 10

result = []

def permutation(word, visited, idx, prev):
    if len(result) >= 1000000:
        return
    visited[idx] = True
    string = prev + word[idx]
    
    not_visit = False
    for i, v in enumerate(word):
        if visited[i] == False:
            not_visit = True
            permutation(word, visited[:], i, string)
    
    if not_visit == False:
        result.append(string)
        
for i in range(10):
    permutation(word, visited[:], i, "")
print(result[-1])