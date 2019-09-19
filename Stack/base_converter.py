from Stack.Stack import Stack
def base_converter(dec_number,base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_String = ""
    while not rem_stack.is_empty():
        new_String = new_String + digits[rem_stack.pop()]

    return new_String

print(base_converter(25,2))
print(base_converter(25,16))
