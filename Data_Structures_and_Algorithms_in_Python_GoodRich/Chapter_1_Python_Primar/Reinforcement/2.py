"""
R-1.2
Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""
# def is_even(k):
#     if (k > 1):
#         k -= 2
#         is_even(k)
#     else:
#         print( True if k == 0 else False)

def is_even(k):
    print( True if k & 1 == 0 else False)

k = int(input("Enter a number: "))
is_even(k)

