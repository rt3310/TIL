fibo = [1, 1]

index = 2
while True:
    next_fibo = fibo[index - 1] + fibo[index - 2]
    fibo.append(next_fibo)
    index += 1
    if len(str(next_fibo)) == 1000:
        print(index)
        break