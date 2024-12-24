#program to find the factorial of a number

n = int(input("Enter the number : "))
fact = 1
while ( n > 1 ):
    fact = fact * n 
    n -=1
    
print(fact)
