"""
P-1.29 Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""
from itertools import permutations

def allStrings(characters):
    perms = [''.join(char) for char in permutations(characters)]
    print(list[set(perms)])

characters = ['c','a','t','d','o']
allStrings(characters)