def get_string_sum(string):
    result = 0
    for i in string:
        result += ord(i) - 64
    return result

with open("/Users/seowonho/TIL/algorithm/euler/names.txt", "r") as f:
    names = list(map(
            lambda x: get_string_sum(x),
            sorted(f.read().replace("\"", "").split(","))
            ))
    
    for i, v in enumerate(names):
        names[i] = v * (i+1)
        
    print(sum(names))