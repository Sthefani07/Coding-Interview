# ---- RETURN STATEMENT
# Function are even more extensible then they seem. 
# Instead os just printing a value, you can also return a value from a function. 
# This allows you to use the result of a function in other parts of your code, outside of the original function.

#ex:
def add_number(x, y):
    return x + y

result = add_number(4, 4) 
print(result)              #output: 8
print("-----")

#---

def product(a, b):
    return a * b

print(product(2, 4))  #output: 8
print(product(8, 2))  #output: 16
print(product(4, 8))  #output: 32
print(product(8, 8))  #output: 64
print("-----")
