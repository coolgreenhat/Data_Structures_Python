"""
Write a Python class that extends the Progression class so that each value
in the progression is the square root of the previous value. (Note that
you can no longer represent each value with an integer.) Your construc-
tor should accept an optional parameter specifying the start value, using
65, 536 as a default.
"""
from math import  sqrt

class Progression:
    def __init__(self,start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return  answer

    def __iter__(self):
        return self

    def print_progression(self,n):
        print(' '.join(str(next(self))for j in range(n)))

class sqrtProgression(Progression):
    def __init__(self,first=65536):
        super(sqrtProgression,self).__init__(first)
        self._prev = first
        self._current = sqrt(first)

    def _advanced(self):
        self._prev, self._current = self._current, sqrt(self._current)

if __name__ == '__main__':
    sqrtProgression().print_progression(4)