"""
This is module for testing get_max_value() function.
"""
from max_of_list import get_max_value


def test_positive():

    test_data = ['5', 'some text', 'nine', '9', '3.5', '12k', '9']
    assert get_max_value(test_data) == 9


def test_negative():

    test_data = ['five', 'two', 'seven', 'ten', 'three']
    assert get_max_value(test_data) is None



def test_float_values():

    test_data = ['25.45', '376.45', '55.3337', '54.5', '782.3']
    assert get_max_value(test_data) == 782
