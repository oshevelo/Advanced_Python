from simple_calc import numbers as num, dates


def main():
    while True:
        try:
            x = int(input('''Enter operation type:
                             1 - mathematical expression
                             2 - operations with dates'''))
        except ValueError:
            print('Available options are 1 and 2')
            continue
        else:
            break
    calc_types = {1: 'numeric',
                  2: 'date'}
    calc_type = calc_types[x]

    if calc_type == 'numeric':
        expression = input('Enter mathematical expression:')
        print(num.evaluate(expression))
    elif calc_type == 'date':
        numbers = []
        operations = []

        counter = dates.count_entries()
        x = dates.enter_date()

        numbers.append(x)

        for i in range(counter - 1):
            while True:
                op = input("Enter operation: ")
                if op not in ['+', '-']:
                    print('Acceptable operations are +, -. Please try again.')
                    continue
                else:
                    break
            operations.append(op)

            while True:
                x = input("Enter next term: ")
                try:
                    x = float(x)
                except ValueError:
                    print("Inputs should be numbers. Please try again.")
                    continue
                else:
                    break
            numbers.append((x))

        print(dates.evaluate_dates(numbers, operations))


if __name__ == "__main__":
    main()
