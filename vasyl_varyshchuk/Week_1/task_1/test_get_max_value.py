from Task_1 import get_max_value


def test_get_max_value():
    assert get_max_value(['5', 'some text', 'nine', '9', '3.5', '12k']) == 9
