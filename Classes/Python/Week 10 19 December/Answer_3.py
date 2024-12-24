# def multiplier(factor):
#     """This function returns a closure that multiplies a number by the given factor. 
# Both inputs come as a product, eg: double,10 = 20
#     """
#     def multiply(number):
#         return number * factor
#     return multiply


# # Get user input for multiplier type
# multiply_type = input()

# # Get user input for number
# number = int(input())

# # Create the appropriate multiplier function based on user input
# if multiply_type == "double":
#     multiply = multiplier(2)
# elif multiply_type == "triple":
#     multiply = multiplier(3)
# else:
#     print("Invalid multiplier type.")
#     exit()

# # Calculate and print the result
# result = multiplier(number)
# print(result)

def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

multiply_single = multiplier(1)
multiply_double = multiplier(2)
multiply_triple = multiplier(3)
multiply_quadruple = multiplier(4)
multiply_quintuple = multiplier(5)

multiply_type = input().strip()
number = int(input().strip())

if multiply_type == "single":
    result = multiply_single(number)
elif multiply_type == "double":
    result = multiply_double(number)
elif multiply_type == "triple":
    result = multiply_triple(number)
elif multiply_type == "quadruple":
    result = multiply_quadruple(number)
elif multiply_type == "quintuple":
    result = multiply_quintuple(number)
else:
    raise ValueError("Invalid multiplier type. Please enter 'single', 'double', 'triple', 'quadruple', or 'quintuple'.")
    

print(result)