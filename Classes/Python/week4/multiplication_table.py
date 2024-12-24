# program to find the multiplication table of a given number

n = int(input("Enter a number : "))
i = 1
while (n > 0 and i <= 10):
    print(f"{n} * {i} = {n*i}")
    i += 1
    
