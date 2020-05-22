#Count no. of spaces in a given text
s = input('Enter the text: ')
count = 0
for i in s:
    if i.isspace() == True:
        count += 1
print('No of spaces:',count)


#Using split()
length = len(s.split())
print('No of spaces:{}'.format(length-1))
