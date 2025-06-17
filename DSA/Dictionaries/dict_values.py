# Dict Values

# Another way of interacting over a dictionary is by using the values() method. This function allows us to loop iver the values in the dictionary without needing to access the keys. It returns a view object that displays a list of all the values in the dictionary.

my_dict = {"a": 1, "b": 2, "c": 3}

for value in my_dict.values():
    print(value)  # Output: 1, 2, 3

# We can also convert the values to a list if we need to work with them as a list. This can be done by using the List() function.

my_dict = {"a": 1, "b": 2, "c": 3}
values = list(my_dict.values())    # Output: [1, 2, 3]

print(values)  # Output: [1, 2, 3]


from typing import Dict, List
def get_dict_values(my_dict: Dict[str, int]) -> List[int]:
    return list(my_dict.values())
# Example usage 



print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))  # Output: [25, 30, 35]
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))  # Output: [25, 30, 35, 40]

