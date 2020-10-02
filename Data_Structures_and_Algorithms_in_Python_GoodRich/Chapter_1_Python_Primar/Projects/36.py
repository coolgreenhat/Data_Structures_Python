"""
P-1.36 Write a Python program that inputs a list of words, separated by white-
space, and outputs how many times each word appears in the list.
"""
from collections import Counter
def WordCount(data):
    print(Counter(data))

wordList = input("Enter a list of words Separated by Spaces: ")
data = wordList.split(' ')
WordCount(data)