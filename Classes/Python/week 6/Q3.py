print("Q3. Sentence Analysis: ")
sentence = input("Enter a sentence: ")
vowels = "AEIOUaeiou"
vowelcount = 0
consonantcount = 0
words = sentence.split()
longestword = ""

for char in sentence:
    if char.isalpha():  # Letter check with alpha :~)
        if char in vowels:
            vowelcount += 1
        else:
            consonantcount += 1

for word in words:
    if len(word) > len(longestword):
        longestword = word

reversesentence = sentence[::-1]
print(f"Vowel count: {vowelcount}")
print(f"Consonant count: {consonantcount}")
print(f"Longest word: {longestword}")
print(f"Reversed sentence: {reversesentence}")


