#!/bin/python3

import os

# #
# # Complete the 'missingCharacters' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.
# #

# def missingCharacters(s):
#     # Define the complete sets of digits and lowercase letters
#     all_digits = set('0123456789')
#     all_letters = set('abcdefghijklmnopqrstuvwxyz')
    
#     # Convert the input string to a set to find present characters
#     present_chars = set(s)
    
#     # Find missing digits and letters by subtracting present characters
#     missing_digits = sorted(all_digits - present_chars)
#     missing_letters = sorted(all_letters - present_chars)
    
#     # Join the missing characters into a single string
#     return ''.join(missing_digits) + ''.join(missing_letters)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()  # Read input string

#     result = missingCharacters(s)  # Call the function with the input string

#     fptr.write(result + '\n')  # Write the result to the output file

#     fptr.close()  # Close the file


#


import os

#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    """
    Transforms a sentence according to the given algorithm.

    Args:
        sentence: The input sentence.

    Returns:
        The transformed sentence.
    """

    # Split the sentence into words
    words = sentence.split()

    # Initialize a list to store the transformed words
    transformed_words = []

    # Initialize a string to store the transformed word
    transformed_word = ""
    
    # Iterate through each word in the sentence
    for word in words:
        # Add the first character of the word to the transformed word string (unchanged)
        transformed_word += word[0]

        # Iterate through the remaining characters in the word
        for j in range(0, len(word) - 1):
            # Compare the current character with the previous character (in lowercase)
            if word[j].lower() < word[j + 1].lower():
                # If the previous character is less than the current character, convert the current character to uppercase
                transformed_word += (word[j + 1].upper())
            elif word[j].lower() > word[j + 1].lower():
                # If the previous character is greater than the current character, convert the current character to lowercase
                transformed_word += (word[j + 1].lower())
            else:
                # If the previous character is equal to the current character, keep the current character unchanged
                transformed_word += word[j + 1]

        # Add the transformed word to the list of transformed words
        transformed_words.append(transformed_word)

        # Reset the transformed word string for the next word
        transformed_word = ""

    # Initialize a string to store the final transformed sentence
    result = ""

    # Join the transformed words back into a single string
    for word in transformed_words:
        result = result + " " + word

    # Remove any leading or trailing spaces from the final sentence
    return (result.strip())

# Test Cases
print(transformSentence("a Blue MOON"))  # Output: a BLUE MOON
print(transformSentence("ab CB GG"))  # Output: aB cb GG
print(transformSentence("x y z"))  # Output: x y z


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open the output file specified by the environment variable

    sentence = input()  # Read input sentence from standard input

    result = transformSentence(sentence)  # Call the function with the input sentence

    fptr.write(result + '\n')  # Write the result to the output file

    fptr.close()  # Close the file

