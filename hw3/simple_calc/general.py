from simpleeval import simple_eval

constants = {'pi': 3.14,
             'e': 2.71}


def count_entries():
    while True:
        try:
            counter = int(input("Enter number of terms: "))
        except ValueError:
            print('Should be a positive integer number. Please try again.')
            continue
        if counter < 2:
            print("Operation can't be performed on less than 2 numbers")
            continue
        else:
            break
    return counter


def evaluate(numbers, operations):
    operations.append(' ')
    numbers = [constants[value] if value in ['pi', 'e'] else value for value in numbers]
    expression = ''.join([str(a) + b for a, b in zip(numbers, operations)])
    return simple_eval(expression)

