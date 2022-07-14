while True:
    number = str(int(input()))
    
    if number == "0":
        break
    
    for i in range(len(number)):    
        if number[i] != number[len(number) - 1 - i]:
            print('no')
            break
    else:
        print('yes')