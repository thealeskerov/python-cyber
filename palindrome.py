# This program checks if a word is a palindrome

word = input("Enter a word: ")

# Reverse the word and compare
if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
