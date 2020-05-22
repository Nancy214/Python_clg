# Create a list that stores number from 1-20. Separate the elements into two list, one for odd and other for even
list1 = []
list2 =[]
list3 = []
for i in range(1, 21):
    list1.append(i)
print('List 1 :',list1)

for no in list1:
    if no%2 == 0:
        list2.append(no)
    else:
        list3.append(no)

print('List 2:',list2)
print('List 3:',list3)
    
