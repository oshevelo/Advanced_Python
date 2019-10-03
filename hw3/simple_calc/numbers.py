from simpleeval import simple_eval, NameNotDefined

constants = {'pi': '3.14',#Fixme: https://docs.python.org/3.6/library/math.html#constants better map to thees 
             'e': '2.71'}


def evaluate(expression):
    expression = expression.replace('pi', constants['pi'])
    expression = expression.replace('e', constants['e'])
    try:
        result = simple_eval(expression)
    except NameNotDefined:
        result = 'Evaluation error. Next time use numbers and math operators +, -, *, /'
    return result
