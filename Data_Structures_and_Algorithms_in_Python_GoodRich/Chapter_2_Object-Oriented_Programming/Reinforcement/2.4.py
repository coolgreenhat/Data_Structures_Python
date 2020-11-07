"""
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its num-
ber of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""
class Flower:
    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def __get_name__(self):
        return self._name

    def __get_petals__(self):
        return self._petals

    def __get_price__(self):
        return self._price

    def  __set_name__(self,name):
        self._name = name

    def __set_petals__(self,petals):
        self._petals = petals

    def __set_price__(self,price):
        self._price = price
