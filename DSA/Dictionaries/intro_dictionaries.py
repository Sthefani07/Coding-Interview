# Intro to Dictionaries in Python
# Dictionaries are a built-in data type in Python that allow you to store key-value pairs. They are also known as associative arrays or hash maps in other programming languages.                               

# Dictionaries are one of the most important data type in Python
#They are used to store {key: value} pairs, The simplest way of thinking about them is a table with two columns, one for keys and one for values.

# KEY    |    VALUE
# --------|----------
#   "Alice"    |    25
#   "Bob"      |    30
#  "Charlie"  |    35                         

my_dict = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}


# ----------------

my_dict = {} # here we are creating an empty dictionary
# We can add key-value pairs to the dictionary using square brackets

my_dict["Alice"] = 25
my_dict["Bob"] = 30     
my_dict["Charlie"] = 35

# AS shown above, to declare an empty dictionary we can use curly braces {}. We can the add key-value pairs to the dictionary using square brackets []  and the assignment operator =. This is similar to list, but key dont have to be integers.

# ----------------

# ex: 

from typing import Dict, List

def create_dict(name: str, age: int) -> Dict[str, int]:
    my_dict = {name: age} # Create a new dictionary with the given name and age
    return my_dict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    my_dict = {}  # Create an empty dictionary
    for i in range(len(words)):
        w = words[i]
        my_dict[w] = i
    return my_dict  # Return the dictionary with words as keys and their indices as values


print(create_dict("Alice", 25))  # Output: {'Alice': 25}
print(create_dict("Bob", 30))    # Output: {'Bob': 30}
print(create_dict("Charlie", 35))  # Output: {'Charlie': 35}

print(list_to_dict(["alice", "bob", "charlie"]))  # Output: {'alice': 0, 'bob': 1, 'charlie': 2}