l = input()
string = input()

number = 0
for i, v in enumerate(string):
    number += ((ord(v) - 96) * (31**i))

print(number % 1234567891)