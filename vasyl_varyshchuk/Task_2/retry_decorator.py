"""
This module implements a function retry decorator
"""

RETRIES = 4


def my_decorator(func):

    def func_wrapper():
        for i in range(0, RETRIES):
            try:
                func()
                break
            except Exception:
                print('Restart => {}'.format(i+1))

    return func_wrapper


@my_decorator
def some_function():
    raise Exception
    print('This text will not printed.')


some_function()
