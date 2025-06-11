# Dict Remove


# You can remove an item from a dictionary using the pop() function. This function takes a key as an argument and removes the key-value pair from the dictionary. If the key does not exist, it will raise a keyError

my_dict = {"a": 1, "b": 2, "c": 3}
my_dict.pop("a")  # Removes the key "b" and its associated value

print(my_dict)  # Output: {'b': 2, 'c': 3}

#print(my_dict.pop("d")) # Raises KeyError: 'd' as 'd' is not in the dictionary
print("-------")

# in case we dont want to be handling with the KeyError, we can use the pop() with a second argument, which will be returned if the key is not found in the dictionary.

my_dict = {"a": 1, "b": 2, "c": 3}

print(my_dict.pop("d", 0))  # Output: 0,        since 'd' is not in the dictionary
print("-------")
# Another way to delete from a dictionary is to use the del statement

my_dict = {"a": 1, "b": 2, "c": 3}
del my_dict["a"]  # Removes the key "a" and its associated value
print("-------")
#another ecample:

from typing import Dict, List

def remove_key_from_dict(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for k in keys:
         if k in my_dict:
             my_dict.pop(k)
    return my_dict


print(remove_key_from_dict({"a": 1, "b": 2, "c": 3}, ["a", "c"]))  # Output: {'b': 2}
print(remove_key_from_dict({"a": 1, "b": 2, "c": 3}, ["d"]))  # Output: {'a': 1, 'b': 2, 'c': 3}