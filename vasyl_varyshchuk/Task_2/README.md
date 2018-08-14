In this task, it is needed to create a decorator which retry the function if an error occurred during its execution. The number of function retries must be specified as a global variable, and also transmitted to the decorator. Another part of the task is to create a decorator that caches the values when the function runs several times.
To solve this task three different function decorators has been implemented. All solution consists of three modules:

    - decorator which retries function that might fail during execution. In this case, a number of retries are defined as a global variable and then used inside the decorator function.

    - retry decorator with the ability to pass a number of retries as decorator parameter. If the parameter is not passed to the decorator, number of retries is equal to None by default.

    - decorator which caches data after function re-run. This module contains function as a decorator to store the square of numbers which have already been calculated.

