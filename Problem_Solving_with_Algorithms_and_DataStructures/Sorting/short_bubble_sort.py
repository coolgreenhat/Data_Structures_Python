"""
A bubble sort can be modified to stop early if it finds that the list has become sorted. 
This means that for lists that require just a few passes, a bubble sort may have an advantage 
in that it will recognize the sorted list and stop.
"""
def short_bubble_sort(a_list):
	exchanges = True			# Set exchanges to True
	pass_num = len(a_list) - 1	# Set pass_num equal to length of the list - 1
	while pass_num > 0 and exchanges:	# While pass_num is greater than 0 and exchanges is True
		exchanges = False				# Set exchanges to False
		for i in range(pass_num):		
			if a_list[i] > a_list[i + 1]:	# If Number in a list is greater than next Number
				exchanges = True			# Set Exchanges to true
				temp = a_list[i]			# Swap Numbers
				a_list[i] = a_list[i + 1]
				a_list[i + 1] = temp
			pass_num = pass_num - 1			# Decrement pass_num by 1

a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(a_list)
print(a_list)

