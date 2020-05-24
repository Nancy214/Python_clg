#Stack operations
class Stack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        if not self.arr:
            return 'Stack is empty'
        return self.arr.pop()

    def peep(self):
        if not self.arr:
            return 'Stack is empty'
        return self.arr[-1]

l = Stack()
i =0
while i != 4:
    print('1.Push\n2.Pop\n3.Peep\n')
    ch = int(input('Enter choice: '))
    if ch == 1:
        element = input('Enter element to be pushed: ')
        l.push(element)
        print(l.arr)
    elif ch == 2:
        print(l.pop())
        print(l.arr)
    elif ch == 3:
        print(l.peep())
        print(l.arr)
    else:
        print('Enter valid choice')
