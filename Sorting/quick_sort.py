def quick_sort(a_list):
	quick_sort_helper(a_list,0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
	if first < last :
		
		split_point = partition(a_list, first, last)

		quick_sort_helper(a_list, first, split_point - 1)
		quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
	pivot_value = a_list[first]

	left_mark = first + 1
	right_mark = last
