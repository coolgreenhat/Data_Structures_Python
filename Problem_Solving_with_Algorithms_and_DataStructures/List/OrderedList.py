from node import Node

class OrderedList:
	def __init__(self):
		self.head = None	# Create An Empty List

	## Search Method
	def search(self, item):
		current = self.head	# Set current reference to head
		found = False	
		stop = False
		
		while current != None and not found and not stop: # While current reference is not None And found is False and stop is False
			if current.get_data() == item:
				found = True
			else:
				if current.get_data() > item:	# Once the value in the node becomes greater than the item we are searching for, the search can stop and return False.
					stop = True
				else:
					current = current.get_next()	# Set Current Reference to Next Field Value
		
		return found

	def add(self, item):
		current = self.head
		previous = None
		stop = False

		while current != None and not stop:		# While Current Reference is Not at End of list And True
			if current.get_data() > item:		# If Data Field referenced by current field is greater than item
				stop = True						# Set stop to True
			else:
				previous = current
				current = current.get_next()

		temp = Node(item)
		if previous == None:
			temp.set_next(self.head)
			self.head = temp
		else:
			temp.set_next(current)
			previous.set_next(temp)



