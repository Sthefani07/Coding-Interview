# ----------------------- STRING FORMATTING ----------------------------

# We saw that we can concatenate string using the + operator. However, this can be cumbersome when we have many strings to concatenate. Python provides a more elegant way to format strings using the format method.

# FOrmat method on the string and pass in the values we want to replace the placeholders with.

name = "Alice"
age = 25

msg = "Hello, {}. You are {} years old.".format(name, age)

print(msg) # output: Hello, Alice. You are 25 years old.
print("-----")

# another ex: 

name = "Sthefani"
age = 29

msg = f"Hello, {name}. You are {age} years old."
print(msg)
print("-----")

def say_goodbye(name: str, hour: int) -> str:

    return f"Goodbye, {name}, See you again at {hour} o'clock."

print(say_goodbye("bob", 12))
print(say_goodbye("Holden", 4))
print(say_goodbye("Sabrina", 9))
print("-----")
