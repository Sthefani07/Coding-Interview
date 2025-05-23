# ------------- STRING INDEXING  ----------------
# if i want to access individual characters from a string. I can do this by indexing the string

my_str = "Hello"
print(my_str[0])  #Output: H
print(my_str[1])  #Output: e
print(my_str[2])  #Output: l
print(my_str[3])  #Output: l
print(my_str[4])  #Output: o
print("-----")

# another ex:

def print_last_char(word: str) -> None:
    last_index = len(word) - 1 
    print(word[last_index])

print_last_char("Sthefani D")    # Output: D
print("-----")
