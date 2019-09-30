import operator
from datetime import timedelta


def evaluate_dates(dates, operation):
    start_date = dates.pop(0)

    operations = {
        '+': operator.add,
        '-': operator.sub,
        }

    result = None

    for i in range(len(dates)):
        result = operations[operation[i]](start_date, timedelta(days=dates[i]))
        start_date = result

    return result.strftime('%Y-%m-%d')
