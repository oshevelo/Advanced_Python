import operator


def calc(x, y, operation):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return 'Inputs should be numbers. Please try again.'

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv}

    if operation not in ['+', '-', '*', '/']:
        return 'Acceptable operations are +, -, *, /. Please try again.'

    return operations[operation](x, y)

x = input("Enter first number: ")
y = input("Enter second number: ")
op = input("Enter operation: ")

print(calc(x, y, op))

