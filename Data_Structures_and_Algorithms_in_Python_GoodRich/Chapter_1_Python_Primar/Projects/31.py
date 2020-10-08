"""
P-1.31 Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""
def makeChange(charged,given):
    change = given - charged
    tens = 0
    fives = 0
    ones = 0
    if change > 10:
        while change > 10:
            change -= 10
            tens += 1
    if change > 5:
        while change > 5:
            change -= 5
            fives += 1
    if change > 0:
        while change > 0:
            change -= 1
            ones += 1
    print("{} notes of ten, {} notes of five, {} notes of one".format(tens, fives, ones))

charged = int(input("Charged Amount: "))
given = int(input("Given amount: "))
makeChange(charged,given)