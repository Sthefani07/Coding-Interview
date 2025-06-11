# Dict Looping

# You can use len() to get the length of a dictionary. This will return the number of KEY-VALUE pairs in the dictionary.

my_dict = {"a": 1, "b": 2, "c": 3}
print(len(my_dict))  # Output: 3
print("-------")

# But just like with SETS,  the length of a dictionary  wont help us to loop over it. The good news is that looping over a dictionary is very similar to looping over a set

my_dict = {"a": 1, "b": 2, "c": 3}

for Key in my_dict:
    value = my_dict[Key]
    print(Key, value)
print("-------")



# By using the for loop, we can iterate over the keys in the dictionary by using the "in" operator. We can then use the key to access the value associated with that key

# We can also use the items() method to loop over both keys and values at the same time.

#exemple:
for key, value in my_dict.items():
    print(key, value)
print("-------")

# another example:

from typing import Dict, List

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    result = []
    for name in age_dict:
        result.append(name)
    return result



# Example usage:
def get_dict_value(age_dict: Dict[str, int] ) -> List[int]:
    result = []
    for value in age_dict:
        age = age_dict[value]
        result.append(age)
    return result



dict_1 = {"Alice": 30, "Bob": 25, "Charlie": 35}
dict_2 = {"Sthef": 27, "Debora": 28, "Ana": 29}

print(get_dict_keys(dict_1))  # Output: ['Alice', 'Bob', 'Charlie']
print(get_dict_value(dict_2))  # Output: [27, 28, 29]


# Another example:
# Take the tring word and return a dictionary with the coynt of each character in word. The key should be the character and the value should be the count of that character in the word.

from typing import Dict

def count_characters(word: str) -> Dict[str, int]:
    count = {}
    # Initialize the dictionary with each character in the word
    for char in word:
        if char not in count:
            count[char] = 0
        else:
            count[char] = count[char] + 1

    return count 


print(count_characters("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(count_characters("world"))  # Output: {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1}
print(count_characters("hello world")) # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print(count_characters("this is a longer sentene")) # Output: {'t': 1, 'h': 2, 'i': 2, 's': 3, ' ': 3, 'a': 1, 'l': 1, 'o': 1, 'n': 1, 'g': 1, 'e': 1}