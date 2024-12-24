# program to find the sum of digits of a number

n = int(input(" Enter the number : " ))
sum1 = 0 
while ( n > 0 ):
    temp_dig = n % 10 
    sum1 = sum1 + temp_dig
    n = n // 10

print(sum1)
