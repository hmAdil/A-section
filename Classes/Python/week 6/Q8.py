print("Q8. repeating chars")    
input_str = input("Enter a string: ")
char_count = {}

for char in input_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char in input_str:
    if char_count[char] == 1:
        print(f"{char} is not repeated.")
    else:
        print(f"{char} is repeated {char_count[char]} times.")




