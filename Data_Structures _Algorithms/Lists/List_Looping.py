# ----------------------- LIST LOOPING ----------------------------

# We can also loop through lists similar t how we loop through strings:

# By using the length of the list:
my_list = [1, 2, 3, 4, 5]

length = len(my_list)

for i in range(length):
    print(my_list[i])
print("-----")     # Output: 1 2 3 4 5 

    # Or by using the "in" operator :

my_list = [1, 2, 3, 4, 5]  

for element in my_list:
    print(element)
print("-----")  # Output: 1 2 3 4 5 

#another ex: how many times does x appear in this input?

from typing import List # used to add type hint for list

def count_x(nums: List[int], x: int) -> int:
    result= 0
    for n in nums:
        if n == x:
            result = result + 1
    return result        

print(count_x([1, 2, 5, 6, 5], 5))    #output: 2
print(count_x([4, 3, 6, 1, 6], 5))    #output: 0
print(count_x([4, 7, 7, 6, 7, 6], 7)) #output: 3
print("-----")

