# Dictionaries cannot contain duplicate keys. just like sets.

my_dict = { "a": 1, "b" : 2, "c": 3 }

print(my_dict["a"])  # Output: 1

my_dict["a"] = 4  # Update the value for key "a"
print(my_dict["a"])  # Output: 4 
print("-------")   

#-------------------

# As shown above, if we assing the same key a new value, the old value is overwritten
# the value within a dictionary can be of any type, including lists, sets, or even other dictionaries. Look at the example below:

my_dict = {"a": [1, 2, 3], "b": {4, 5, 6}, "c": {"x": 1, "y": 2, "z": 9}}

print(my_dict["a"])  # Output: [1, 2, 3]
print(my_dict["b"])  # Output: {4, 5, 6}
print(my_dict["c"])  # Output: {'x': 1, 'y': 2, 'z': 9}
print("-------") 
#-------------------



your_dict = {
    "a": 10,
    "apple": 20,
    "bat": 7
}

print(your_dict)
print(your_dict["a"]) # Output: 10
print("d" in your_dict) # Output: False
your_dict["a"] = 4
print(your_dict["a"]) # Output: 4
print("-------") 

