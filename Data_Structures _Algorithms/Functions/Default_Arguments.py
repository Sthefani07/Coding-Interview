#------ DEFAULT ARGUMENTS
# you can specify default values for the parameters in a function definition. In the code below, we have the parameter name a default value of "world". If we call the funtion without any arguments, the default value will be used. If we call the function with a argument will be used instead.


def greet(name="world"):            #PS: The = iqual sign is important here
    print("Hello, " + name + "!")

greet()                             #Output: "Hello, world!"
greet("Bob")                        #Output: "Hello, Bob!"    
print("-----")


def greet(greeting="Hello", name="world"):   # This is valid 
    print( greeting + ", " + name + "!")


def greet(greeting, name="world"):           # This is valid as well 
    print( greeting + ", " + name + "!") 


# def greet(greeting="Hello", name):            # This is NOT valid
#     print( greeting + ", " + name + "!")    

print("-----")