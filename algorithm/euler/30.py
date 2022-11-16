
result = set()
for i in range(999):
    for j in range(999):
        check = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        mul = i * j
        complete = True
        for n in str(i):
            if int(n) < 1 or check[int(n)-1] == 1:
                complete = False
                break
            check[int(n)-1] = 1
        for n in str(j):
            if int(n) < 1 or check[int(n)-1] == 1:
                complete = False
                break
            check[int(n)-1] = 1
        for n in str(mul):
            if int(n) < 1 or check[int(n)-1] == 1:
                complete = False
                break
            check[int(n)-1] = 1
        if complete and sum(check) == 9:
            print(i, j, result)
            result.add(mul)

print(result)
print(sum(result))