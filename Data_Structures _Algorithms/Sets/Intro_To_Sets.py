# ----------------------- INTRO TO SETS ----------------------------------

# In Python a SET is very similar to a LIST, with a few key differences.

# A set is unordered, meaning the element are not stored in a specific order. If order is important, you should use a list. Cause order in sets can be unpredictable

# a SET can only contain unique elements. If you try to add a duplicate elemente to a set, it will be ignored.

# example:

my_set = {1, 2, 3}
print(my_set) #output: {1, 2, 3}
print("-----")

my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print(my_set) #output {1, 2} Repare que o segundo (1) foi ignorado
print("-----")


from typing import List, Set

def list_to_set(nums: List[int]) -> Set[int]:
    my_set = set()
    for n in nums:
        my_set.add(n)
    return my_set

print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
print("-----")

