n = 1

while (n <= 30 ):
    if( n % 3 == 0 and n % 5 == 0 ):
        print("fizz buzz", n)
    
    elif (n % 5 == 0):
        print("buzz" , n )
    
    elif ( n % 3 == 0 ) :
        print("fizz " , n )
    
    n += 1
