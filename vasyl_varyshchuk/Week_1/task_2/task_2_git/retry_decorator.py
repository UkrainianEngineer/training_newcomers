"""
This module implements a decorator which restarts the function for specified number of times
if an error occurred during its execution.
"""
RETRIES = 4


def decorator(func):

    def func_wrapper():

        i = 0
        while i < RETRIES:
            try:
                func()
            except Exception:
                i += 1
            print('Restart => {}'.format(i))

    return func_wrapper


@decorator
def some_function():
    raise Exception
    print('I am a function.')


some_function()
