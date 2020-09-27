"""
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""
def sumSquare(n):
    print(sum([i*i for i in range(n)]))

n = int(input("Enter a Number: "))
sumSquare(n)