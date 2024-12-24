from arithmetic import add, mul, div, sub
# from arithmetic import *

try:
    a,b=int(input("Enter Number a: ")), int(input("Enter Number b: ")) 
    print("Addition: ", add(a,b))
    print("Subtraction: ", sub(a,b))
    print("Multiplication: ", mul(a,b))
    print("Division: ", div(a,b))
except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Division Error: Division by zero is not allowed")

import arithmetic as am
print("\nValue of Gravitational acceleration on earth is: ",am.gravity)




