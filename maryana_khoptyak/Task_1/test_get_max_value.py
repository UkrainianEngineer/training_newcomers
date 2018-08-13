EMPTY_SEQUENCE = []
ONLY_ONE_ELEM_NUM = ["15"]
ONLY_ONE_ELEM_CHR = ["some  long text goes here"]
ONLY_CHR = ["one", "two", "ten", "some  long text goes here"]
ONLY_NUMBERS = ["1", "2", "10", "15", "-2", "16.9"]
DATA = ["one", "1", "two", "2", "ten", "10", "15", "-2", "some  long text goes here", "16.9", "&"]


def get_max_value(data):
    """ Function which returns a maximum integer value from list of strings """
    sorted_nums_list = []
    for value in data:
        try:
            sorted_nums_list.append(float(value))
        except ValueError:
            pass
    if sorted_nums_list:
        return max(sorted_nums_list)
    else:
        None


def test_empty_sequence():
    assert get_max_value(EMPTY_SEQUENCE) is None, ("The is no elements in sequence, your list is", EMPTY_SEQUENCE )


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
