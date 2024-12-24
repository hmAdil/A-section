Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 0b100
4
\
>>> # ^ bitwise x or return true if inputs are not same
>>> print(7^4)
3
>>> print(1^1)
0
>>> print(2^9)
11
>>> 
>>> '''
... membership operator
... collections in python -> list,tuple,set,dictionary
... '''
'\nmembership operator\ncollections in python -> list,tuple,set,dictionary\n'
>>> a=[10,20,30]
>>> b=[1,'Ram',89.56]
>>> print(type(a))
<class 'list'>
>>> print(type(b))
<class 'list'>
>>> print("Ram" in b)
True
>>> print(90 in b)
False
>>> print(90 not in b)
True
>>> print(10 not in a)
False

>>> student{1:'Ram',2:'Krish',3:'Radha'}
SyntaxError: invalid syntax
>>> student={1:'Ram',2:'Krish',3:'Radha'}
>>> print(1 in student)
True
>>> a = 10
>>> b = 20
>>> c = 30
>>> print(a is b)
False
>>> print(a is not c)
True
>>> '''
... Assignment operator
... a = 5 ,= is assignment
... '''
'\nAssignment operator\na = 5 ,= is assignment\n'
>>> \+=,-=,*=,/=,//=,%=,**=
SyntaxError: unexpected character after line continuation character
>>> #+=,-=,*=,/=,//=,%=,**=
>>> # a+= 10 a=a+10
>>> a=10
>>> b=7
>>> a+=10
>>> print(a)
20
>>> b-=5
>>> print(b)
2
>>> b*+a
40
>>> print(b)
2
>>> b*=a
>>> print(b)
40
