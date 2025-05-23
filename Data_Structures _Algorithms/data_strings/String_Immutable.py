# ----------------------- STRINGS ARE IMMUTABLE ----------------------------

# it's important to know that whenever you slice a string, you are not modifying the underlying string. Instead, you are creating a new string with the sliced characters. This is because strings are immutable in Python, which means they cannot be changed after they are created.

message = "I will never change."

#message[0] = "x" # This will cause a error

# In the code above, we cannot change individual characters, we can only reassing the entire srting.
 
 # another ex:

message = "I will never change."

before_second = message[:1] # "I"
after_second = message[2:]  #"Will never change."

new_message = before_second + after_second
print(new_message)
print("-----")

#another ex:

def remove_fourth_character(word:str) -> str: #we will remove the fourth index
    first_part = word[:3]
    second_part= word[4:]
    return first_part + second_part


print(remove_fourth_character("Seattle"))
print(remove_fourth_character("Bellevue"))
print("-----")

