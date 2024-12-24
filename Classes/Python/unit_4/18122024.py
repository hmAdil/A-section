# from doctest import testmod
# #import testmod
# # define a function to test
# def fact(n):
#     '''
#     >>> fact(5)
#     120
#     >>> fact(0)
#     1
#     >>> fact(4)
#     12
#     '''
#     if n==0:
#         res=1
#     else:
#         res=n*fact(n-1)
#     return res

# #calling the testmod function
# testmod(name="fact", verbose=False)




import pdb
def fact(n):
    f=1
    for i in range(1,n+1):
        #pdb.set_trace()
        print(i)
        f*=i
    return f
print("Factorial of 5 = ",fact(5))