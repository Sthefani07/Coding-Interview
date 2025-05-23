# ----------------------- REVERSING A STRING ----------------------------
# We can also slicing to reverse a string. By not specifying the starting of the index or the ending index, and setting the step to -1, the string will be reversed.

my_string = "Hello"

print(my_string[::-1]) # output: olleH
print("-----")

#another ex:

my_string = "Hello"
start, end, step = 1, 4, 1

#print(my_string[start:end])       # output: ello

print(my_string[start:end:-1])   # output: lle

#another ex:

def reverse_string(input_string:str) -> str:
    return input_string[::-1]

print(reverse_string("Seattle"))   # output: elttaeS
print(reverse_string("Sthefani"))  # output: inafehtS
print(reverse_string("Hello"))     # output: olleH
print("-----")
