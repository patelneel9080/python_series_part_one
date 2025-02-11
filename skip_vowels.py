# Create a program that:
# Iterates over a string (e.g., "PYTHON").
# Uses a continue statement to skip vowels and print only consonants.

for i in "PYTHON":
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
        continue
    print(i)
