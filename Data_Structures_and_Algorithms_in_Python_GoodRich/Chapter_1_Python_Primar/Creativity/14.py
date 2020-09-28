"""
C-1.14 Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""
def distinctPair(data):
   product = [[i*j for i in data if i != j] for j in data]
   flatproduct = [item for sublist in product for item in sublist]
   for i in flatproduct:
       if i & 1:
           print(True)

data = [1,2,4,5]
distinctPair(data)