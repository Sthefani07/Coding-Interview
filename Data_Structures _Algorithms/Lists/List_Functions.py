# ----------------------- LIST FUNCTIONS ----------------------------

# Python also provides some built in functions to get the sum, minimum, and maximum of a list:

my_list = [1, 2, 3, 4, 5]

print(sum(my_list)) #Output: 15
print(min(my_list)) #Output: 1
print(max(my_list)) #Output: 5
print("-----")

# 1* The sum() funtion returns the sum of all the elements in the list
# 2* The min() function returns the smallest element in the list.
# 3* The max() function returns the largest element in the list.

#another ex:

from typing import List

def get_sum(my_list: List[int]) -> int:
    total = 0
    for n in my_list:
        total += n 
    return total

def get_min(my_list: List[int]) -> int:
    min_num = my_list[0]
    for n in my_list:
        if n < min_num:
            min_num = n
    return min_num

def get_max(my_list: List[int]) -> int:
    max_num = my_list[0]
    for n in my_list:
        if n > max_num:
            max_num = n
    return max_num


print(get_sum([1, 2, 3, 4, 5]))  #Output: 15
print(get_sum([5, 4, 5, 6]))     #Output: 20
print("-----")
print(get_min([7, 3, 4, 5]))     #Output: 3
print(get_min([5, 4, 5, 6]))     #Output: 4
print("-----")
print(get_max([7, 3, 4, 5]))     #Output: 7
print(get_max([7, 9, 4, 1]))     #Output: 9
print("-----")