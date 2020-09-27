"""
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.

R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""
def sumOddSquare(n):
  print(sum([i*i for i in range(n) if i % 2 != 0]))

n = int(input("Enter a Number: "))
sumOddSquare(n)