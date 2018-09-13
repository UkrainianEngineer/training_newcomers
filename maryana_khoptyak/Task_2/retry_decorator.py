"""
The module implements 'retry' decorator.
If some part of code in decorated function fails, it will be re-run again for number of retries that is passed
as decorator parameter or until function executes successfully.
If decorated function executes successfully, it will not be re-run.
"""

import random
list_of_fruits = ("banana", "strawberry", "lemon", "pineapple", "apple", "coconut", "watermelon")
FAVORITE_FRUIT = "strawberry"

def decorator_with_params(retries):
    def decorator(func):
        def wrapper(list_with_items):
            choice = func(list_with_items)
            if choice != FAVORITE_FRUIT:
                for _ in range(retries):
                    choice = func(list_with_items)
                    if choice == FAVORITE_FRUIT:
                        print("WOHOO! You guessed my favorite fruit {} from {} retry".format(choice.upper(), _+1))
                        return None
                    else:
                        print("This is your {} retry and choice is: {}".format(_+1, choice))
                print("Oh, no! You didn't guess my favorite fruit (((")
            else:
                print("GREAT JOB! You guessed my favorite fruit from first time")

        return wrapper
    return decorator

@decorator_with_params(retries=4)
def guess_favorite_fruit(list_of_fruits):
    returned_choice = random.choice(list_of_fruits)
    return returned_choice

if __name__ == "__main__":
    guess_favorite_fruit(list_of_fruits)
