# Write a program to implement all arithmetic operators:
print('Operations:\n 1.Addition\n 2.Subtraction\n 3.Product\n 4.Divison\n 5.Remainder\n')

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))

op = input('Enter operation number: ')
if op == '1':
    result = n1+n2
    print('Addition of {} and {} is {}'.format(n1,n2,result))

elif op == '2':
    result = n1-n2
    print('Subtraction of {} and {} is {}'.format(n1,n2,result))

elif op == '3':
    result = n1*n2
    print('Product of {} and {} is {}'.format(n1,n2,result))

elif op == '4':
    result = n1/n2
    print('Divison of {} and {} is {}'.format(n1,n2,result))

elif op == '5':
    result = n1%n2
    print('Remainder of {} and {} is {}'.format(n1,n2,result))
