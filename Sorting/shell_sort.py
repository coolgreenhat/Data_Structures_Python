def shell_sort(a_list):
	
	sublist_count = len(a_list) // 2	# Create a Sublist_count set to half the size of Original List (Say 4 for list length 9)
	
	while sublist_count > 0:		# While Sublist_count is greater than 0
		
		for start_position in range(sublist_count):		# Running for loop on sublist_count(4)
			gap_insertion_sort(a_list, start_position, sublist_count)	# Call function gap_insertion sort on Say (a_list, 0, 4)

		print("After increments of size", sublist_count, "The list is", a_list)	# Print the list after first iteration
	
		sublist_count = sublist_count // 2		# Set Sublist_count to half of Current sublist_count

def gap_insertion_sort(a_list, start, gap):			# Start position(0) is taken as start and sublist count(4) is taken as gap
	for i in range(start + gap, len(a_list), gap):		# Running for loop on sublist i.e for i in range (0 + 4, 9, 4)
		current_value = a_list[i]						# Set Current value to element at index i(4) in a_list
		position = i									# set position equal to i(4)

		while position >= gap and a_list[position - gap] > current_value:	# While position is greater than or equal to gap And element at index in a_list[4 - 4] is greater than current value
			a_list[position] = a_list[position - gap]	# element in sublist is set as preceding element to sublist
			position = position - gap					# set position equal to preceding position 

		a_list[position] = current_value				# Set preceding element to current value

a_list = [54, 26, 93, 17, 77, 31, 44, 55,20]
shell_sort(a_list)
print(a_list)


