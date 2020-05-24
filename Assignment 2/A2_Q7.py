#Stack operations
flag = 1
l =[]
def push(l):
    n = input('Enter the element to be pushed: ')
    l.append(n)
    print(l)

def pop(l):
    l.pop()
    print(l)

def peep(l):
    print('Top element is ',l[0])
    
while (flag == 1):
    print('1.Push')
    print('2.Pop')
    print('3.Peep')
    
    op = int(input('Enter operation no: '))
    if op == 1:
        push(l)
        break
    elif op == 2:
        pop(l)
        break
    elif op == 3:
        peep(l)
        break
    flag = int(input('Enter 1 to continue and 0 to quit: '))
