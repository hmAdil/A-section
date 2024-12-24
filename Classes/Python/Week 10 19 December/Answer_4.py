
def valid_pos(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be a positive number")
        if x < -10**6 or x > 10**6:
            raise ValueError("Input must lie within -10^6 & 10^6")
        return func(x)
    return wrapper

@valid_pos
def sq_root(x):
    return x ** 0.5

x = float(input())

try:
    result = sq_root(x)
    print(result)
except ValueError as e:
    print(f"ValueError: {str(e)}")



'''
Method 2:
import math

def validate_positive(f):
    def wrap(x):
        # Check if x is within the specified range and is positive
        if x <= 0 or x < -1000000 or x > 1000000:
            raise ValueError("Input must be a positive number")
        return f(x)
    return wrap

@validate_positive
def square_root(x):
    return math.pow(x, 0.5)

x = float(input())
try:
    res = square_root(x)
    print(res)
except ValueError as e:
    print("ValueError:", str(e))
'''