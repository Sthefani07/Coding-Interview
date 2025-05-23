# ----------------------- LIST POP ----------------------------

# We can also remove elements from a list using the pop() function.

my_list = [1, 2, 3]

my_list.pop()
print(my_list) #OUtput: [1, 2]
print("-----")

# We can also specify an index to remove a specific element, as shown below

my_list = [1, 2, 3]
my_list.pop(0)
print(my_list) #Output: [2, 3]

my_list.pop(1)
print(my_list)  #Output: [2]
print("-----")

#another ex:

from typing import List

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    my_list.pop(index)
    return my_list

print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))
print("-----")

def pop_n_from_list(my_list: List[int], n:int) -> List[int]:
    while n > 0:
        my_list.pop()
        n = n-1
    return my_list


print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print("-----")
