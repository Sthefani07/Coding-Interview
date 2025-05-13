# FUNCTION
def greet():    # greet() = This will be print "Hello world!" 
    print("Hello, world!")

def say_goodbye():
    print("Goodbye, World!")

greet()
say_goodbye() 

print("-----")



# FUNCTION DECLARATION
# Similar to how variable must be declared before they can be used, 
# functions must also be declare before they can be called
#-----------------------
#print(n) # error because n is not defined yet
#n = 10

#print_number(5) # error because the function print_number is not defined yet

#def print_number(n):
#    print(n)

#-----------------------   

def print_number(n):
    print(n)

print_number(10) #output: 10
print_number(20) #output: 20
print("-----")

#------- PARAMETERS
# in the code below we defined a function called that greet1() that takes a 
# PARAMETER called "name". We  call the funtion by passing in 
# "Sthefani" as the argument. 

def greet1(name): 
    msg = "Hello, " + name
    print(msg)

greet1("Sthefani")   #Output Hello, Sthefani / Argument
greet1("Nick")       #Output Hello, Nick / Argument
greet1("Holden")     #Output Hello, Holden / Argument
print("-----")

#-----MULTIPLE PARAMETERS
#function can be defined to accept more than one parameter. 
# The parameters are separated by commas in the function definition.
# When calling the function the arguments are also separeted by commas.

def greet(name, greeting):
    message = greeting + " " + name
    print(message)

greet("Alice", "Hello")                             # output: Hello Alice
greet("Nick", "I hope you had a great day today,")  # output: I hope you had a great day today, Nick
print("-----")
#-- another ex: ----

def two_sum(sum1, sum2):
    #print(sum1, sum2)   #output: 10 9 basicamente so print o numero
    print(sum1 + sum2)  #output: 19

def three_sum(sum1, sum2, sum3):
    #print(sum1, sum2, sum3)        #output: 5 14 6 / basicamente so print o numero que esta dentro da function
    print(sum1 + sum2 + sum3)      #output: 25

two_sum(10, 9)          #output: 19
two_sum(7, 10)          #output: 17
three_sum(5, 14, 6)     #output: 25
three_sum(3, 5, 8)      #output: 16
print("-----")