# ----------------------- LIST OPERATOR ----------------------------

#List can also be used within conditional statements. For example, we can check if a list is empty or not:

my_list = [1, 2, 3]

if len(my_list) > 0:
    print("The list is not empty")

else:
    print("THe list is empty.")

# We can also use the "in" operator to check if an element is present in a list:


my_list = [1, 2, 3]

if 2 in my_list:  # if 2 is in my list, then do .... 
    print("2 is in the list")
else:
    print("2 is not in the list")    

#another ex: ------

def check_list_empty(my_list) -> bool:
    if len(my_list) == 0:
        return True
    return False

#or the same example below in a shorter version:
def check_list_empty(my_list) -> bool:
    return len(my_list) == 0 
print("-----")

#another ex: ------
def check_element_in_list(my_list, element) -> bool:
    if element in my_list:
        return True
    return False

#or the same example below in a shorter version:
def check_element_in_list(my_list, element) -> bool:
    return element in my_list


print(check_list_empty([]))
print(check_list_empty([1, 2, 3]))

print(check_element_in_list([1,2, 3], 1))
print(check_element_in_list([1, 2, 3], 4))
print("-----")