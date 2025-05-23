# ----------------------- SET OPERATIONS ----------------------------------

# We can also perform Various operations on sets in Python. We can remove elements from a set using the remove() function. If the element is not present in the set , a KeyError will be raised

my_set= {1, 2, 3}

my_set.remove(2)
print(my_set) # Output: {1, 3}

#my_set.remove(4)     # Raised a KeyError

# Just like with list, we can loop over elements with a set using "for" loops. The difference is that we cant access elements by index because sets are unordered. The order that we loop over a set is not guaranteed