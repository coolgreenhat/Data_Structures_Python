def bubble_sort(a_list):
	for pass_num in range(len(a_list) - 1, 0, -1):	# for a value in range list length - 1 to zero  
		for i in range(pass_num):					# for i in range value
			if a_list[i] > a_list[i + 1]:			# if element at position i is greater than next element 
				temp = a_list[i]
				a_list[i] = a_list[i + 1]
				a_list[i + 1] = temp				# Swap elements

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)
