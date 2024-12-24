# import math as mt

# try:
#     a=int(input("Enter a number whose factorial must be found out: "))
#     print(mt.factorial(a))
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except RecursionError:
#     print("Factorial of the number is too large to handle.")

# import sys
# print(sys.path)
# sys.path.insert(0)

def add():
    '''This is addition program on integer input.'''
    x,y=int(input("Enter Number x: ")), int(input("Enter Number y: ")) 
    '''In addition function'''
    return x+y

def sub():
    '''This is subtraction program on integer input.'''
    x,y=int(input("Enter Number x: ")), int(input("Enter Number y: ")) 
    '''Inside subtraction function'''
    return x-y
print(add.__doc__); print("Sum:",add()); print(sub.__doc__); print("Difference:",sub())