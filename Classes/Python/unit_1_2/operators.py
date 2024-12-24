Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
arithemetic operators
three types unary, binary and ternary
**(exponent or power), %(modulus)
'''
'\narithemetic operators\nthree types unary, binary and ternary\n**(exponent or power), %(modulus)\n'
a=10
b=20
print(a+b)
30
#int,int then the answer is int
#int, float then the result is float.
a = 30
b = 20.2
print(a-b)
9.8
>>> a=15
>>> print(a-b)
-5.199999999999999
>>> c=5
>>> d=7
>>> print(c*d)
35
>>> k=35
>>> m=7
>>> print(k/m)
5.0
>>> #true division will always give you a float.
>>> m=56
>>> n=18
>>> print(m//n)
3
>>> m= 56.2
>>> n=18.0
>>> print(m//n)
3.0
>>> #it will always give you the result in int and float. In float it will only give the int value and not the decimal value.
>>> a=2
>>> b=4
>>> print(a*b)
8
>>> print(a**B)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(a**B)
NameError: name 'B' is not defined. Did you mean: 'b'?
>>> print(a**b)
16
>>> b=4.0
>>> print(a**b)
16.0
>>> a=8
>>> b=3
>>> print(a%b)
2
>>> b=3.0
>>> print(a%b)
2.0
>>> #relational operators
>>> #it gives you the result as boolean value true or false
>>> #<,>,<=,>=,==,!=\
>>> a=20
>>> b=15
>>> print(a<b)
False
>>> print(a>b)
True
>>> print(a<=c)
False
>>> print(a<=b)
False
>>> c=20
>>> print(a<=c)
True
>>> print(a>=c)
True
>>> print(a==c)
True
>>> print(a!=c)
False
>>> # if condition true then true otherwise false
>>> x = int(input("Enter a number: "))
Enter a number: 3
>>> x = int(input()
...         4
...         
SyntaxError: incomplete input
>>> x = int(input())
...         
x = int(input())4
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x = int(input())
ValueError: invalid literal for int() with base 10: 'x = int(input())4'






