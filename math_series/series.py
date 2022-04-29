def series(num):
    return '1'


'''
Create a function called fibonacci. The function should have one parameter n. 
The function should return the nth value in the fibonacci series. 
You may implement the function using recursion or iteration. 
If you are feeling particularly frisky, do both as separate functions.
'''


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


'''
In your series.py module, add a new function lucas that returns the nth value in the lucas numbers. 
Again, you may use recursion or iteration, or both. 
Again, ensure that your function has a well-formed docstring.
'''

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


'''
Add a third function called sum_series with one required parameter and two optional parameters. 
The required parameter will determine which element in the series to print. 
The two optional parameters will have default values of 0 and 
1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the fibonacci series. 
Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. 
Other values for the optional parameters will produce other series. 
Again, you may use recursion or iteration, or both. 
Again, ensure that your function has a well-formed docstring.
'''


def sum_series(n, m=0, p=1):
    if n == 0:
        return m
    elif n == 1:
        return p
    else:
        return sum_series(n - 1, m, p) + sum_series(n - 2, m, p)
