"""
This module implements a retry decorator with ability to pass a parameter into decorator
"""

import random


def decorator(retries=None):

    def my_decorator(func):

        def func_wrapper():
            if retries is not None:
                for i in range(1, retries+1):
                    try:
                        func()
                        break
                    except Exception:
                        print('Restart => {}'.format(i))
            else:
                func()

        return func_wrapper

    return my_decorator


@decorator(retries=4)
def some_function():
    print('Text Before Exception')
    i = random.randint(1, 10)
    if i > 5:
        raise Exception
    else:
        print('This text prints when exception is not raised, i = {}'.format(i))
    


some_function()
