# ------ TYPE HINTS
# This is not required, but it can be helpful for other developers who are reading your code.
#  It indicate what type of data the function expects to receive and return.

def add(x: int, y: int) -> int:
    return x + y

#ex:

def greet(name: str) -> None:
    print("Hello " + name)
    return

print(type(greet("Sthefani")))  
print("-----")