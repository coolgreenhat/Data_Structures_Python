def insertion_sort(a_list):
	for index in range(1, len(a_list)): # for a range 1 to length of the list

		current_value = a_list[index]	# Set Current Value equal to List element at given Index
		position = index			# Set position equal to index

		while position > 0 and a_list[position - 1] > current_value:	# While Position is greater than 0 and Number preceding Current value is greater than current value
			a_list[position] = a_list[position - 1]		# Set Number at Given position equal to Number Preceding given value
			position = position - 1						# Set position equal to preceding position

		a_list[position] = current_value	# Set Value at preceding position equal to current value

a_list = [54,26,93,17,77,31,44,55,20]
insertion_sort(a_list)
print(a_list)
