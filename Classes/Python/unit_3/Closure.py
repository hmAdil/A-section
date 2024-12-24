##def outer(msg):#This is the outer enclosing function
##    def inner():#This is nested function
##        print(msg)
##    return inner#returns the nested function#it returns the id of inner to the different variable through outer function
##different=outer("This is an example of closure")
##different()#refers to inner()
##
###CONTROL/DRY RUN OF THE ABOVE CODE
##
##def outer(msg):#2
##    def inner():#5
##        print(msg)#6
##    return inner#3
##different=outer("This is an example of closure")#1
##different()#4
##
##
##
##
###nested function
##def f1():
##    print('in f1')
##    def f2():
##        print('in f2')
##    f2()
##    print(id(f1))
##    print(id(f2))
##f1()
##
##
##
###CLOSURE-IT IS A NESTED FUNCTION 
##def f1(x):
##    print("in f1")
##    print("x=",x)
##    y=20
##    print("y in f1",y)
##    def f2():
##        print("in f2")
##        z=30
##        print("x in f2",x)
##        print("y in f2",y)
##        print("z in f2",z)
##    print(id(f1))
##    print(id(f2))
##    return f2
##closure=f1(x=34)
##closure()
##
##
###EVEN IF THE OUTER FUNCTION IS DELETED STILL INNER FUNCTION WILL WORK AND WILL RETURN THE OUTPUT
##def f1():
##    def f2():
##        print('hello')
##        print('world')
##    return f2
##c=f1()
##del f1
##c()




#MY WORK
"""def fun(x, y) : 
    if x == 0 : 
        return y 
    else : 
        return fun(x - 1, x * y) 
print(fun(4, 2))
"""





def f1():
    x=0
    def f2():
        nonlocal x
        x+=1
        return x
    return f2
c=f1()
print(c())#y=c() print(y)#This will print 1 
print(c())#This will print 2

#inner function should have a fre variable/nonlocal variable not local variable for closures.
