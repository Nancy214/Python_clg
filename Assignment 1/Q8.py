#Print first letter of every word in a string
s = input('Enter the string: ')
words = s.split()
for i in words:
    print('The first letter of "{}" is {}'.format(i,i[0]))

