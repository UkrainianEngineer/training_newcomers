"""
This module implements a retry decorator with ability to pass a parameter into decorator
"""


def decorator(retries=None):

    def my_decorator(func):

        def func_wrapper():
            if retries is not None:
                i = 0
                while i < retries:
                    try:
                        func()
                    except Exception:
                        i += 1
                        print('Restart => {}'.format(i))
            else:
                func()

        return func_wrapper

    return my_decorator


@decorator(retries=4)
def some_function():
    print('Tex Before Exception')
    raise Exception
    print('Text After Exception')
    


some_function()
