"""
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""
def minmax(data):
    smallest = largest = data[0]
    for i in data[1:]:
        if i < smallest:
            smallest = i
        elif i > largest:
            largest = i
    return (smallest, largest)

# n = input("Enter number of digits")
data = [1,4,6,7]
# for _ in n:
#     num = int(input())
#     data.append(num)
print(minmax(data))
