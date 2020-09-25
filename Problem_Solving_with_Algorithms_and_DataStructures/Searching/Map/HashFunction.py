def put(self, key, data):
	hash_value = self.hash_function(key, len(self.slots))	# Calculate has using remainder method

	if self.slots[hash_value] == None:	# If Key is not present then
		self.slots[hash_value] = key	# Add key to the slot List and
		self.data[hash_value] = data	# Add value to the data List

	else:								# else Key is already present
		
		if self.slots[hash_value] == key:	# If Key matches to one already present
			self.data[hash_value] = data	# Replace the data values for given key
		
		else:								# else If Key does not match 
			next_slot = self.rehash(hash_value, len(self.slots))	# Calculate Next Slot using rehash function
			
			while self.slots[next_slot] != None and self.slots[next_slot] != key:	# While Slot indicated by next_slot is not equal to None And Slot indicated by next Slot is Not equal to Key
				next_slot = self.rehash(next_slot, len(self.slots))					# Calculate Next slot using rehash function 

				if self.slots[next_slot] == None:	# If Next slot key is None
					self.slots[next_slot] = key		# Set Key to next_slot
					self.data[next_slot] = data		# Set Data to next_Slot
				else:
					self.data[next_slot] = data		# else Replace data in next slot i.e. If Key is already present

def hash_function(self,key,size):
	return key % size

def rehash(self, old_hash, size):
	return (old_hash + 1) % size

def get(self, key):
	start_slot = self.hash_function(key, len(self.slots))	# Generate hash using hash_function

	data = None
	stop = False
	found = False
	position = start_slot	

	while self.slots[position] != None and not found and not stop: # Traversal
		if self.slots[position] == key:		# if key matches to Key in Slot	
			found = True					# Set found True 
			data = self.data[position]		# Set data equal to element in data list equivalent to Key

		else:
			position=self.rehash(position, len(self.slots))
			if position == start_slot:
				stop = True
	return data

def __getitem__(self, key):
	return self.get(key)

def __setitem__(self, key, data):
	self.put(key, data)


