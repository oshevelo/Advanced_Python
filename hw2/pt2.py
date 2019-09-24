import sys
import operator


def calc(numbers, operation):

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv}



    return operations[operation](x, y)

numbers = []
operation = []


try:
    counter = int(input("Entre number of numbers: "))
except ValueError:
    print('Counter should be an integer number. Please try again.')
    sys.exit()

if counter < 2:
    print("Operation can't be performed on less than 2 numbers")
    sys.exit()

for i in range(counter):
    while True:
        try:
            x = float(input("Enter your number: "))
        except ValueError:
            print("Inputs should be numbers. Please try again.")
            continue
        else:
            break
    numbers.append((x))
    if i < counter-1:
        while True:
            op = input("Enter operation: ")
            if op not in ['+', '-', '*', '/']:
                print('Acceptable operations are +, -, *, /. Please try again.')
            else:
                break
        operation.append(op)

operation.append(' ')

expression = ''.join([str(a) + b for a,b in zip(numbers,operation)])

print(eval(expression))
