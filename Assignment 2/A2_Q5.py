# Binary Search
l = list(map(int, input('Enter a list: ').split()))
l.sort()
print('The sorted list is: ',l)
element = int(input('Enter element to be found: '))
start = 0
end = len(l)-1
while start <= end:
    mid = (start + end) // 2
    if l[mid] == element:
        print('{} is at index {}'.format(element, mid))
        break
    elif l[mid] < element:
        start = mid + 1
    else:
        end = mid - 1
