# ----------------------- TUPLES ----------------------------------

# Tuples are very simple to lists, but they have on key difference: THEY ARE IMMMUTABLE, ou seja nao pode mudar a sequencia.  This means once a tuple is created, it cannot be changed. We can create a tuple by using parentheses instead of square brackets:

my_tuples = (4, 5, 6)
print(my_tuples)  #Output: (4, 5, 6)

# We can index it just like a list: ---
my_tuples = (4, 5, 6)

print(my_tuples[0])   #Output:  4
print(my_tuples[1])    #Output: 5

# We can also slicing:

my_tuples = (4, 5, 6)
print(my_tuples[1:])  #output: (5, 6)
print("-----")

# WE CANNOT modify a tuple and cannot call append() or POP() since this functions would modify it

# Its common to use tuples to store related data.

from typing import Tuple

def create_pair(name: str, age: int) -> tuple[str, int]:
    return(name, age)


print(create_pair("Alice" , 25))
print(create_pair("Charlie", 30))
print(create_pair("Bob", 35))
print("-----")
