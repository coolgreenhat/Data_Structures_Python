"""
C-1.22 Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
"""
def dotproduct(a,b):
    print ([i[0] * i[1] for i in zip(a,b)])
a = [1,2,3,4]
b = [9,8,7,6]
dotproduct(a,b)
