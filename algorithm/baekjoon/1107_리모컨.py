n = input()
m = int(input())

broken = [0] * 10
for i in list(map(int, input().split())):
    broken[i] = 1

number = ''
if int(n) - 100 <= len(n) or m == 10:
    print(int(n)-100)
elif m == 0:
    print(len(n))
else:
    for i in n:
        count = 0
        while count < 10:
            if broken[int(i)+count] == 0:
                number += str(int(i)+count)
                break
            if broken[int(i)-count] == 0:
                number += str(int(i)-count)
                break
            count += 1
    print(len(str(int(number))) + abs(int(n)-int(number)))
    
# 풀이중