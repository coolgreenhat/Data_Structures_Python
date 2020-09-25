from Deque import Deque

def pal_checker(a_string):
	char_deque = Deque() # Create Deque Object referenced as char_deque

	for ch in a_string:	# Run for loop on given String
		char_deque.add_rear(ch)	# Add each character to the rear of the deque
	still_equal = True	# Set still_equal to True

	while char_deque.size() > 1 and still_equal:	# while deque size is greater than 1 and still_equal is True
		first = char_deque.remove_front()			# Remove Character from front of Deque
		last = char_deque.remove_rear()				# Remove Character from last of Deque
		if first != last:							# If first and last character is Not equal then Set still_equal to False
			still_equal = False

	return still_equal								# Return Value Of still Equal

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
			
