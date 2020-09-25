# Each Node Object holds two Pieces Of Information
# Data Field --> Which holds List item
# Next Field --> Field Which Holds Reference to Next Node

class Node:
	def __init__ (self, init_data):
		self.data = init_data
		self.next = None

	def get_data(self):
		return self.data	# Get Data Field Value

	def get_next(self):
		return self.next	# Get Next Field Value
	
	def set_data(self,new_data):
		self.data = new_data	# Set Data Field Value

	def set_next(self,new_next): 
		self.next = new_next	# Set Next Field Value


