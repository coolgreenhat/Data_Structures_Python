"""
C-1.24 Write a short Python function that counts the number of vowels in a given
character string.
"""
def VowelsCount(str):
    vowels = 0
    count = [1 for i in str if i in ['a','i','e','o','u','A','I','E','O','U']]
    print(len(count))

str = input("Enter a String: ")
str = list(str)
VowelsCount(str)