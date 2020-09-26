"""
R-1.1
  Write a short Python function, is_multiple(n, m), that takes two integer
  values and returns True if n is a multiple of m, that is, n = mi for some
  integer i, and False otherwise.
"""


def is_multiple(n,m):
    print(True if n%m == 0 else False);

n = int(input('Enter a number: '))
m = int(input('Enter another number: '))
is_multiple(n,m)

