
def get_max_value(data):
    """ Function which returns a maximum integer value from list of strings """
    sorted_nums_list = []
    for value in data:
        try:
            sorted_nums_list.append(float(value))
        except ValueError:
            print("The value can't be casted to float type")
    return max(sorted_nums_list) if sorted_nums_list else None
