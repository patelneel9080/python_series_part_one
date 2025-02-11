# Create a program that
# Takes a list of words as input.
# Use list comprehension to create a new list containing only words that start with a vowel.

wordSize = int(input("Enter no. of words you want to input : "))


l = [  input("Enter word : ") for i in range(1,wordSize+1)]

print(l)
