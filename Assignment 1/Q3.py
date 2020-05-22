#Display all prime numbers within range given by user
start = int(input('Enter starting point: '))
end = int(input('Enter ending point: '))
for i in range(start, end+1):
    if i > 1:
        for no in range(2, i):
            if (i%no) == 0:
                break
        else:
            print(i)
            
