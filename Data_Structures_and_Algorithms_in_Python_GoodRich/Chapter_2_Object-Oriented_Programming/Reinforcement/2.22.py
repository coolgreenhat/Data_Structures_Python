"""
2.22 The collections.Sequence abstract base class does not provide support for
comparing two sequences to each other. Modify our Sequence class from
Code Fragment 2.14 to include a definition for the eq method, so
that expression seq1 == seq2 will return True precisely when the two
sequences are element by element equivalent.

2.23 In similar spirit to the previous problem, augment the Sequence class with
method lt , to support lexicographic comparison seq1 < seq2.
"""
from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        """
        Return the length of the sequence.
        """

    @abstractmethod
    def __getitem__(self, j):
        """
        Return the element at index j of the sequence.
        """

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        for j in range(len(self)):
            if self[j] == other[j] :
                return False
        return True

    def __lt__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        for j in range(len(self)):
            if self[j]  > other[j] :
                return False
        return True