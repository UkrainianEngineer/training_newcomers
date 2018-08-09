"""
This is module for testing get_max_value() function.
"""
from max_of_list import get_max_value


def test_get_max_value():

    test_data_1 = ['5', 'some text', 'nine', '9', '3.5', '12k', '9']
    test_data_2 = ['five', 'two', 'seven', 'ten', 'three']

    assert get_max_value(test_data_1) == 9
    assert get_max_value(test_data_2) is None


def test_float_values():

    test_data_3 = ['25.45', '376.45', '55.3337', '782.563', '54.5', '782']
    assert get_max_value(test_data_3) == 782
