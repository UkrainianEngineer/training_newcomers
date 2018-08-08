'''
This module finds maximum integer value from list of strings.

'''
import sys

data = ['one', '1', 'two', '2', 'ten', '10', '15', '-2', 'some long text goes here', '16.9']

def get_max_value(iterable):

    max_value = -sys.maxint

    for x in iterable:
        try:
            if int(float(x)) > max_value:
                max_value = int(float(x))
        except ValueError:
            print("Could not convert '{}' to an integer.".format(x))
    if max_value == -sys.maxint:
        return None
    else:
        return max_value


result = get_max_value(data)
print('\n' +  'Maximum integer value of list: {}:'.format(result))


