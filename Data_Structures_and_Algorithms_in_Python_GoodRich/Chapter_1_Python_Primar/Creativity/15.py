"""
C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""
def distinctNumbers(data):
    if len(data) == len(set(data)):
        print("Given list is distinct")
    else:
        print("Given list is not distinct")


# data = [1,2,4,5,7,8,1,4]
data = [1,4,5,7,8,9]
distinctNumbers(data)