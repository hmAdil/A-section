Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#relational operator
#<,>,<=,>=,==,!=
'car'<'cat'
True
'Car'< 'cat'
True
'car' > 'cat'
False
'cat'>'cattle'
False
'cat'<'cattle'
True
#Logical Operators
#and,or,not
#not is unary and rest are binary
#X AND Y , X OR Y, NOT X , NOT Y
#return is either TRUE or FALSE
(4<5)
True
(4<5) and (6>7)
False
#return is either TRUE or FALSE
#and returns true only when X and Y are true
(4<5) and (6<7)
True
(6>7) or (8>9)
False
(6>7) or (8<9)
True
# or returns true if either X or Y is true
not True
False
not(8<9)
False
not(8>9)
True
(a!=b) and (a>b)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    (a!=b) and (a>b)
NameError: name 'a' is not defined
print((a!=b) and (a>b))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print((a!=b) and (a>b))
NameError: name 'a' is not defined
a = 7
b = 6
print((a!=b) and (a>b))
True
(a!=b) and (a>b)
True
'''
short circuit evaluation
Logical and return False if X is False, it will not evaluate y
Logical or return true if X is True, it will not evaluate y
'''
'\nshort circuit evaluation\nLogical and return False if X is False, it will not evaluate y\nLogical or return true if X is True, it will not evaluate y\n'
'''
bitwise operator
& bitwise and, | bitwise or
~ bitwise not, << bitwise left shift
>> bitwise right shift
~ is unary and rest all are binary
'''
'\nbitwise operator\n& bitwise and, | bitwise or\n~ bitwise not, << bitwise left shift\n>> bitwise right shift\n~ is unary and rest all are binary\n'
0b101
5
0b102
SyntaxError: invalid digit '2' in binary literal
0b100
4
0b110
6
0b111
7
bin(8)
'0b1000'
0h100
SyntaxError: invalid decimal literal
8h100
SyntaxError: invalid decimal literal
hex(10)
'0xa'
bin(23)
'0b10111'
0xa
10
hex(1)
'0x1'
0x2
2
0x3
3
0x8
8
0x9
9
0xb
11
0xc
12
0o1
1
'''
For binary the initials are 0b
For octal the initials are 0o
For hexa the initials are 0x
'''
'\nFor binary the initials are 0b\nFor octal the initials are 0o\nFor hexa the initials are 0x\n'
# bitwise and &
7&4
4
0b1001
9
0b100
4
0b111
7
8& 9
8
8&4
0
7&9
1
0b01
1
# bitwise and & if both are 1 then the answer is 1 otherwise 0

'''
bitwise or if any is 1 the answer is 1 otherwise if both are 0 then 0
'''
'\nbitwise or if any is 1 the answer is 1 otherwise if both are 0 then 0\n'
>>> 7|4
7
>>> 9|3
11
>>> 0b1111
15
>>> 0b1010
10
>>> 0b1011
11
>>> ~4
-5
>>> ~7
-8
>>> '''
... positive numbers are represented in 8-bit
... 4 - 0000,0100
... -4 - 1111,1100
... '''
'\npositive numbers are represented in 8-bit\n4 - 0000,0100\n-4 - 1111,1100\n'
>>> # ~n = -(n+1) where n is any positive number
>>> ~4
-5
>>> ~67
-68
>>> ~23
-24
>>> ~-7
6
>>> # ~-n = -(-n+1)
>>> 
>>> 
>>> #bitwis left shift <<
>>> 
>>> 4<<2
16
>>> 0b110
6
>>> 0b101
5
>>> 0b100
4
>>> 0b10000
16
>>> 6<<3
48
>>> 110000
110000
>>> 0b110000
48
>>> 9<<5
288
>>> bin(288)
'0b100100000'
>>> bin(-4)
'-0b100'
>>> 0b11111100
252
>>> # bitwise right shift >>
>>> 
>>> 4>>2
1
>>> 4>>3
0
>>> 5>>2
1
>>> 5>>5
0
>>> 4>>1
2
>>> 0b01
1
>>> 0b11
3
>>> 23>>2
5
>>> 23>>1
11

