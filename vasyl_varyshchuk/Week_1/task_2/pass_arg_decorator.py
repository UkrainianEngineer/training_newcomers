"""
This module implements a retry decorator with ability to pass a parameter into decorator
"""


def decorator(retries=None):

    def my_decorator(func):

        def func_wrapper():

            i = 0
            while i < retries:
                try:
                    func()
                except Exception:
                    i += 1
                    print('Restart => {}'.format(i))

        return func_wrapper

    return my_decorator


@decorator(retries=4)
def some_function():
    raise Exception
    print('I am a function.')


some_function()