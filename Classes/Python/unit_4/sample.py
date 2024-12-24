import module1
module1.f1()
module1.f2()
module1.f3()
#a=a+10 or a +=10 will throw error
module1.a=module1.a+2 #or maybe module1.a += 2
print('val after update',module1.a)

print('name in sample.py is',__name__)
if __name__=='__main__':
	print("In Module1")
else:
	print("Not in module1")
