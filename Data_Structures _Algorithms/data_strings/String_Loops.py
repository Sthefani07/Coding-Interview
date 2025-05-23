# --------------- STRING LOOP ------------------
# What if we want to access each character in a string separately? 
# With our knowledge of loops, indexing and the len() function we can accomplish this.

my_string = "Hello, World!"

length = len(my_string)  # 13

for i in range(length):
    print(my_string[i])
print("-----")


#another ex:

def print_string_characters(my_str: str) -> None:
    for i in range(len(my_str)):
        print(my_str[i])
print("-----")

print_string_characters("Hello World!")  #call the function
print_string_characters("Good Job!") 
print("-----")
