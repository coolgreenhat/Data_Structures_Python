# Using Python list to implement deque
# Rear of the Deque is at position 0 in list
# Adding and removing items from the front is O(1)
# Adding and removing from the rear is O(n)

class Deque:                         
	def __init__(self):		# Initialize class Deque By Creating Empty
		self.items = []		# list items

	def is_empty(self):		
		return self.items == [] # Check Whether List is Empty or Not

	def add_front(self, item):
		self.items.append(item) # Append item to end of list (front of Deque)

	def add_rear(self, item):
		self.items.insert(0,item) # Insert item at front of list (Rear of Deque)

	def remove_front(self):
		return self.items.pop() # Remove item from end of list (front of Deque)

	def remove_rear(self):
		return self.items.pop(0) # Remove item from front of list (Rear of Deque)

	def size(self):
		return len(self.items)	# Return length of list items

