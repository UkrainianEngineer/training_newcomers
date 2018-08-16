"""Tests for get_max_value are implemented in below module"""

from func_get_max_value import get_max_value

DATA = ["one", "1", "two", "2", "ten", "10", "15", "-2", "some  long text goes here", "16.9", "&"]
EMPTY_SEQUENCE = []
ONLY_CHR = ["one", "two", "ten", "some  long text goes here"]
ONLY_NUMBERS = ["1", "2", "10", "15", "-2", "16.9"]
ONLY_ONE_ELEM_CHR = ["some  long text goes here"]
ONLY_ONE_ELEM_NUM = ["15"]


def test_empty_sequence():
    assert get_max_value(EMPTY_SEQUENCE) is None, "The result is different then expected"


def test_one_number():
    assert get_max_value(ONLY_ONE_ELEM_NUM) == 15, "The result is different then expected"


def test_one_character():
    assert get_max_value(ONLY_ONE_ELEM_CHR) is None, "The result is different then expected"


def test_only_numbers():
    assert get_max_value(ONLY_NUMBERS) == 16.9, "The result is different then expected"


def test_only_characters():
    assert get_max_value(ONLY_CHR) is None, "The result is different then expected"


def test_mixed_data():
    assert get_max_value(DATA) == 16.9, "The result is different then expected"
