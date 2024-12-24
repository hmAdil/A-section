print('In module1')
a=10
def f1():
	print('In f1')
def f2():
	print('In f2')
def f3():
        print('In f3')

print('name in module.py is', __name__)
if __name__=='__main__':
	print('In module1')
else:
	print('Not in module1')
