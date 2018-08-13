To solve this task three different function decorators has been implemented. All solution consists of three modules:

    - decorator which retries function that might fail during execution. In this case, a number of retries are defined as a global variable and then used inside the decorator function.

    - retry decorator with the ability to pass a number of retries as decorator parameter. If the parameter is not passed to the decorator, number of retries is equal to None by default.

    - decorator which caches data after function restart. This module contains function as a decorator to store the square of numbers which have already been calculated.

