'''
Homework 2 splitted to modules
Math constants added (pi, e)
Data type date added
'''

from datetime import datetime
from simple_calc import general as gen, dates


def main():
    counter = gen.count_entries()
    numbers = []
    operation = []
    calc_type = 'numeric'

    while True:
        x = input('Enter first term: ')
        if x in ['pi', 'e']:
            break
        try:
            x = datetime.strptime(x, '%Y-%m-%d')
        except ValueError:
            try:
                x = float(x)
            except ValueError:
                print("Inputs should be a number or a date (yyyy-mm-dd format). Please try again.")
                continue
            else:
                break
        else:
            break

    if isinstance(x, datetime):
        calc_type = 'date'

    numbers.append(x)

    for i in range(counter-1):
        while True:
            op = input("Enter operation: ")
            if calc_type == 'numeric' and op not in ['+', '-', '*', '/']:
                print('Acceptable operations are +, -, *, /. Please try again.')
                continue
            elif calc_type == 'date' and op not in ['+', '-']:
                print('Acceptable operations are +, -. Please try again.')
                continue
            else:
                break
        operation.append(op)

        while True:
            x = input("Enter next term: ")
            if x in ['pi', 'e']:
                break
            try:
                x = float(x)
            except ValueError:
                print("Inputs should be numbers. Please try again.")
                continue
            else:
                break
        numbers.append((x))

    if calc_type == 'numeric':
        print(gen.evaluate(numbers, operation))
    elif calc_type == 'date':
        print(dates.evaluate_dates(numbers, operation))


if __name__ == "__main__":
    main()
