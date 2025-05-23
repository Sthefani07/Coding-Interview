# ----------------------- LIST APPEND ----------------------------

# We can do more than just change individual elements within a list. We can also add new element to the end of the list using the append() function.

my_list = [1, 2, 3]
print(my_list) #output: [1,2,3]

my_list.append(4)
print(my_list) # Output: [1,2,3,4]
print("-----")

# A few thing to notice:

# 1* We can print an a entire list at once.

# 2* The append() function adds an element to the end to the list. This is not a separate function, it's called with a period after the list name (append()). This is called a method. It is a function that is associated with a specific object(in this case a list is an object). 

# 3* After calling append, the original list has been modified to include the new element at the end. The length increased from 3 to 4.


#ex: It should append(add to the end of the list) each number from elements to the end of the my_list and return the modified list.

from typing import List

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:

    for n in elements:
        my_list.append(n)
    return my_list

print(append_to_list([1, 2, 3], [4, 5])) #Output: [1, 2, 3, 4, 5]
print(append_to_list([], [1, 2, 3, 4]))  #Output: [1, 2, 3, 4]
print("-----")
