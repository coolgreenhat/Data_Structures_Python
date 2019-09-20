def selection_sort(a_list):
	for fill_slot in range(len(a_list) - 1, 0, -1): # for value in range length of list - 1 to 0 
		pos_of_max = 0		# Set Max position at 0
		for location in range(1, fill_slot + 1):	# for location in range 1 to value + 1
			if a_list[location] > a_list[pos_of_max]: 	# if Number at given location is greater than Number at Max position
				pos_of_max = location					# Set Max position to given Number 
		
		a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot] # Swap greater Number and max_position Number 

a_list = [54,26,93,17,77,31,44,55,20]
selection_sort(a_list)
print(a_list)


