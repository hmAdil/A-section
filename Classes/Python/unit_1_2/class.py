'''
n=int(input('Enter a number: '))
result =''
while n!=0:
    rem=n%2
    result=str(rem)+result
    n=n//2
print('Binary is',result)
'''
'''
n=int(input('Enter a number: '))
reverse=0
while n!=0:
    d=n%10
    reverse=reverse*10+d
    n=n//10
print('Reverse',reverse)
'''
'''
n=int(input('Enter a number: '))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print('Sum',sum)
'''

i=1
while i<=10:
    if i%2!=0:
        print('odd number is ',i)
    else:
        print('even number is ',i)
        i=i+1
print('thats all')
