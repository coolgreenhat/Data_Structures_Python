"""
P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""
def divisionByTwo(n):
    count = 0
    while n >= 2:
        n = n/2
        count += 1
    print(count)

divisionByTwo(8)