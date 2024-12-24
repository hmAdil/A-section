def f1(f3):
    print(id(f3))
    print("in f1")
    f3()
def f2():
    print(id(f2))
    print("in f2")
f1(f2)
print(id(f1))


def process_data(data, calback):
    result=[d*2  for d in data]
    calback(result)
#Call the callback function with the result
def print_result(result):
    print("Processed data:", result)
data=[1,2,3]
process_data(data, print_result)




def function(func_list,x,y):
    print("Inside function")
    for func in func_list:
        func(x,y)
def add(x,y):
    z=x+y
    print("Sum=",z)
def divide(x,y):
    z=x/y
    print("Quotient=",z)
cb_list=[add,divide]
function(cb_list,10,5)
    




def cab(book,x,y):
    for i in book:
        i(x,y)
def ola(x,y):
    print("Source",x," to destination using ola",y)
def uber(x,y):
    print("Source",x," to destination using uber",y)
book=[ola,uber]
cab(book,"jammu","punjab")




