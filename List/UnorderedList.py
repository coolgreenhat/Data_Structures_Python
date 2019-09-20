from node import Node

class UnorderedList:
	
	def __init__(self):
		self.head = None   # By Default Set head Value To None 
	
	def is_empty(self):
		return self.head == None	#  Check Whether head value is equal To None Which Shows that there are No Nodes in List

	def add(self,item):
		temp = Node(item)	# Creates a new node and places the item as its data
		temp.set_next(self.head)	# changes the next reference of the new node to refer to the old first node of the list.
		self.head = temp	# Set head of the list to refer to the new node

# Linked List Traversal
# Traversal refers to the process of systematically visiting each node.

	def size(self):
		current = self.head		# External Reference is called current and is Initialized to te head of te list
		count = 0	
		while current != None:	# While Current Reference doesn't hold value None
			count = count + 1	# Increment Count By 1 and
			current = current.get_next() # Set current reference to Next Field i.e. Next Node.

		return count


	def remove(self, item):
		current = self.head	# Set Current reference to head Node
		previous = None	# Set previous reference to None
		found = False	# set found as False
	##### Searching the List #####
		while not found:	#  While found is not True 
			if current.get_data() == item:	# if data field referenced by Current reference is equal to item
				found = True	# Set found as True
			else: ## Using "inch-worming" process i.e. previous must catch up to current before current moves ahead
				previous = current	# else set Previous reference as Current and 
				current = current.get_next()	# Set Current reference to Next Node
	##### Removing the Node #####
		if previous == None:			# If previous Reference is None i.e. item to be removed is first item in list
			self.head = current.get_next()	# change head Value to Next field from Current Reference i.e. Second Node
		else:
			previous.set_next(current.get_next()) # Else Set Next field from previous reference to Next field from Current Reference

