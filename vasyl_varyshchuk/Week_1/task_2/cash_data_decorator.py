"""
This module implements decorator which caches data after function restart.
"""


def cash_decorator(func):

    cash = {}

    def wrapper(arg):

        if arg not in cash:
            cash[arg] = func(arg)
            print('Calculated value => {}'.format(cash[arg]))
            return cash[arg]
        else:
            print('Using data from the cash => {}'.format(cash[arg]))
            return cash[arg]
    return wrapper


@cash_decorator
def square(x):
    return x**2


square(2)
square(5)
square(2)
square(2)
square(5)


