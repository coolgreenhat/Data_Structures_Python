def ordered_sequential_search(a_list, item):
	pos = 0
	found = False
	stop = False

	while pos < len(a_list) and not found and not stop: # While pos is less than length of list and not found is True and not stop is True
		if a_list[pos] == item:				# If Item is found in List 
			found = True					# Set Found to true
		else:	
			if a_list[pos] > item:			# If Item is smaller than Item in list
				stop = True					# Set stop to True
			else:
				pos = pos + 1				# Increment pos

	return found						

test_list = [0,1,2,8,13,17,19,32,42,]
print(ordered_sequential_search(test_list,3))
print(ordered_sequential_search(test_list,13))


