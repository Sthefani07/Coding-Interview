# ----------- STRING SLICING PART 1 ----------------------------
# If we only want to access a portuon of a string we can slicing. Slicing allows us to extract a substring frm a string by soecifying a range of indices.

my_string = "Hello, world!"

start, end = 1,5

print(my_string[start:end]) # output: ello
print("-----")

#another ex:

def get_substring(input_string:str, start: int, end:int) -> str:
    if end > len(input_string):
        return ""
    
    return input_string[start:end]

print(get_substring("SeattLe", 1,7))
print(get_substring("SeattLe", 1,8))
print(get_substring("SeattLe", 1,9))
print(get_substring("SeattLe", 0,2))
print(get_substring("SeattLe", 0,7))
print("-----")

# ----------------------- STRING SLICING PART 2 ----------------------------
# if we dont specify the start, it's equivalent to starting from the beginning of the string

my_string = "Seattle"

print(my_string[:3])   #output: Sea
print(my_string[0:3])  #output: Sea
print("-----")
#if we don't specify the end, it's equivalent to ending at the end of the string

my_string = "Seattle"

print(my_string[3:])   #output: Sea
print(my_string[3:7])  #output: Sea
print("-----")

#another ex:

def first_n_characters(s:str, n:int) -> str :
    return s[:n]

def last_n_characters(s:str, n:int) -> str:
    index = len(s) - n
    return s[index:]

print(first_n_characters("Seattle", 3))
print(first_n_characters("Seattle", 4))
print(first_n_characters("Seattle", 7))
print("-----")
print(last_n_characters("Seattle", 3))
print(last_n_characters("Seattle", 4))
print(last_n_characters("Seattle", 7))
print("-----")

