#Divide by 0 and file not found exception
def div(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print('Denominator cannot be 0')
        

def file(file_name):
    try:
        f = open(file_name)
    except FileNotFoundError:
        print("File not Found")
    f.close()


x = int(input('Enter numerator: '))
y = int(input('Enter denominator: '))
div(x,y)

file_name = input('Enter file name: ')
file(file_name)
