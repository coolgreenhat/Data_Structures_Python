# Using List As A Stack And Top is at the Beginning of the list.
class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
         return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

s = Stack()
s.push('hello')
s.push('true')
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size())