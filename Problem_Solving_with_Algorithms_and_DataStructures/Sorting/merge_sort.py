def merge_sort(a_list):
	print("Splitting ", a_list)
	if len(a_list) > 1:		# If length of the list greater than 1
		mid = len(a_list) // 2	# Split list in middle
		left_half = a_list[:mid] # Set left half of list equal to list index from 0 to mid - 1
		right_half = a_list[mid:]	# Set right half of the list equal to list index from mid to last
		
		merge_sort(left_half)	# Recursively call merge_sort on left half of the list
		merge_sort(right_half)	# Recursively call merge_sort on right half of the list

		i = 0
		j = 0
		k = 0

		while i < len(left_half) and j < len(right_half): # while i is less than length of left list and j is less than length of right list 
			if left_half[i] < right_half[j]:			  # if i th element of left_half is smaller than j th element of right half 
				a_list[k] = left_half[i]				  # set k th element of a_list as left_half[i]
				i = i + 1								  # increment i by 1
			else:										  # Otherwise 
				a_list[k] = right_half[j]				  # set k th element of a_list as j th element of right_half
				j = j + 1								  # increment j by 1
			k = k + 1									  # increment k by 1

		while i < len(left_half):						  # while i is less than length of left list 
			a_list[k] = left_half[i]					  # set k th element of a_list to i th element of left_half
			i = i + 1									  # increment i by 1		
			k = k + 1									  # increment k by 1

		while j < len(right_half):						  # while j is less than length of right_half
			a_list[k] = right_half[j]					  # set k th element of a_list as j th element of right_half	
			j = j + 1									  # increment j by 1
			k = k + 1									  # increment k by 1
	print("Merging ", a_list)							  

a_list = [54,26,93,17,77,31,44,55,20]
merge_sort(a_list)
print(a_list)

