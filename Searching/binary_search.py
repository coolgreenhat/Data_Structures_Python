def binary_search(a_list,item):
	first = 0		
	last = len(a_list) - 1
	found = False

	while first <= last and not found:	# While first is smaller than or equal to last and not found is True
		midpoint = (first + last) // 2	# find Middle position of list
		if a_list[midpoint] == item:	# If middle position element is equal to item
			found = True				# Set found True
		else:							
			if item < a_list[midpoint]:	# if item is smaller than element at midpoint
				last = midpoint - 1		# set last equal to  midpoint - 1
			else: 
				first = midpoint + 1	# else set first equal to midpoint + 1

	return found							

test_list = [0,1,2,8,13,17,19,32,42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))

