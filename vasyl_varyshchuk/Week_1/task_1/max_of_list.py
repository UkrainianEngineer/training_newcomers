'''
This module finds maximum integer value from list of strings.

'''

data = ['one', '1', 'two', '2', 'ten', '10', '15', '-2', 'some long text goes here', '16.9', '&']

def get_max_value(iterable):

    numbers = []

    for item in iterable:

        try:
            numbers.append(int(float(item)))
        except ValueError:
            print("Could not convert '{}' to an integer.".format(item))

    if len(numbers) != 0:
        return max(numbers)
    else:
        return None


result = get_max_value(data)
print('\n' +  'Maximum integer value of list: {}:'.format(result))


