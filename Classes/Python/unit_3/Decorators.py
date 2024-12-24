"""def func_decorator(func):
    def inner_func():
        print("Hello,before the function starts")
        func()
        print("Hello after the function is called")
    return inner_func
def func_hello():
    print("Hello inside function")
hello=func_decorator(func_hello)
hello()
""""""

def f1(f):
    x=1
    print("Value of x =",x,"and id of f =",id(f))
    def f2():
        print("Inside f2 x is",x)
        f(x)
        print("Hello World")
    return f2

def func_hello(a):
    print("Inside func_hello x is",a)
c=f1(func_hello)
c()


@f1
def func_hello(a):
    print("Inside func_hello x is",a)
func_hello()
"""
import math
def cal(f):
    def inner(*arg):
        print("Decorator")
        f(*arg)
        print("*******")
    return inner
@cal
def factorial(num):
    print(math.factorial(num))
@cal
def squareroot(num):
    print(math.sqrt(num))
@cal
def minimum(*num):
    print(min(num[0],num[1],num[2]))
factorial(5)
squareroot(16)
minimum(1,2,3)
