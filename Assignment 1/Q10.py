#Make a list of odd numbers in range 1-100. Find the sum of them
print('List of odd numbers in range 1 to 100 is:\n')
odd_sum = 0
for i in range(1, 101):
    if i%2 != 0:
        print(i)
        odd_sum += i
print('The sum of odd numbers from 1 to 100 is {}'.format(odd_sum))
        
