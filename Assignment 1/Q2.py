#Write a program to find largest of three numbers given by users
print('Enter three numbers:')
n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))
n3 = int(input('Number 3: '))

if n1 > n2 and n1 > n3:
    print('{} is largest of the three numbers'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} is largest of the three numbers'.format(n2))
else:
    print('{} is largest of the three numbers'.format(n3))
