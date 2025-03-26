message = "This is a message."
print(message)

capital_of_spain = "Spain"
print(capital_of_spain)
print("-----------------")


python_creation_date = "February, 1991"
java_creation_date = "May, 1995"
javascript_creation_date = "December, 1995"
Sthefani_born_date = "October, 1995"

print(python_creation_date)
print(java_creation_date)
print(javascript_creation_date)
print(Sthefani_born_date)
print("---------------")

msg1, msg2 = "World", "Hello"
msg3, msg4, msg5 = "Name", "Is", "My"
# rename the variable so it will print (Hello world) & (My name is), lembrar to manter o variable in the same position e apenas mudar o resultado = renomeado
msg1, msg2= msg2, msg1
msg3, msg4, msg5 = msg5, msg3, msg4,

print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print("---------------") 

# Variable Types
age = 29                  # Integer / Numero inteiro
temperature = 75.6        # floating-point number
is_true = True            # boolean
name = "Sthef"            # string
my_list = [1, 2, 3,4]     # list

print(type(age))
print(type(temperature))
print(type(is_true))
print(type(name))
print(type(my_list))
print("---------------") 

# exercicio: the acordo com o print(type(variable)) tentar replicar p codigo a cima
variable = 1
print(type(variable))

variable = 1.1
print(type(variable))

variable = False
print(type(variable))

variable = "abc"
print(type(variable))

variable = []
print(type(variable))
print("---------------") 

# Another challenge is reassing the variable to print a integer / numero inteiro
pi = 3.748798759
square_root_8 = 2.759874
#  code below
pi = int(pi)
square_root_8 = int(square_root_8)

print(pi)
print(square_root_8)
print("---------------") 

# Eu posso converter uma sting (numero) para integer da forma feita abaixo
variable = "10" 
print(type(variable))

variable = int(variable)
print(type(variable))
print("---------------") 

# Arithmetic Operators

x , y = 3, 6

print(x + y)    # Output : 9    integer 
print(x - y)    # Output : -3
print(x * y)    # Output : 18
print(x / y)    # Output : 0.5  float number
variable = int(variable)
print(type(variable))
print("---------------") 

## Exercise 
a, b, c = 2, 2, 0.5

total_sum = a + b + c # giving a name to the variable
total_product = a * b * c

print(total_sum)
print(0 - total_sum)
print(a * b * c)
print(total_sum / total_product)
print("---------------") 

# MORE OPERATORS
        # Floor division : //
        # Modulus : %
        # Exponentiation : **

# Here is a exemplo:
x, y = 7, 2  

print(x // y) # Output : 3 ( 7 divided by 2 is 3.5, after rounding donw we get 3)
print(x % y)  # Output : 1 (7 divided by 2 is 3, with a remainder of 1)
print(x ** y) # Output : 49 (7 raised to the power of 2 is 49, 7*7 = 49)
print("---------------") 

## Exercise 
 
a, b, c = 2, 8, 5

product_a_b = a * b
print(product_a_b // c)
print(product_a_b % c)
print(a ** b)
print(b ** c)
print("---------------")

# Shorthand Operator
count = 0
count = count + 1
count = count + 2
print(count)  # Output : 3
print("---------------")

# Boolean "OR" = BAsicamente if one of the boolean is true the answer always will be TRUE. 
#         Thuth table
#  |  A        B        A or B    |
#  |  False    False      False   |
#  |  True     False      True    |
#  |  False    True       True    |
#  |  True     True       True    |

a, b, c, d = False, False, True, True

print(a or b)             #output False
print(b or c)             #output True
print(c or d)             #output True
print(a or b or c or d)   #output True
print("---------------")

#  BOOLEAN "AND" = Basicamente is TRUE only when they both are TRUE
##         Thuth table
#  |  A        B        A or B    |
#  |  False    False      False   |
#  |  True     False      False   |
#  |  False    True       False   |
#  |  True     True       True    |

a, b, c, d = False, False, True, True

print(a and b)             #output False
print(b and c)             #output False
print(c and d)             #output True
print(a and b and c and d) #output False
print("---------------")

# BOOLEAN NEGATION

a = True
b = False
print(not a)          #output: False
print(not b )         #output: True
print(not(a and b))   #output: True
print("---------------")
a, b, c = False, False, True
print(not c)           #output: False
print(not(a and b))    #output: True
print(not(b or c))    #output: True used    "or"
print(not(b and c))    #output: False used "and"
print("---------------")

# FUNCTION
def greet():    # greet() = This will be print "Hello world!" 
    print("Hello, world!")

def say_goodbye():
    print("Goodbye, World!")

greet()
say_goodbye() 

print("---------------")



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
print("---------------")

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
print("---------------")

#-----MULTIPLE PARAMETERS
#function can be defined to accept more than one parameter. 
# The parameters are separated by commas in the function definition.
# When calling the function the arguments are also separeted by commas.

def greet(name, greeting):
    message = greeting + " " + name
    print(message)

greet("Alice", "Hello")                             # output: Hello Alice
greet("Nick", "I hope you had a great day today,")  # output: I hope you had a great day today, Nick
print("---------------")
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
print("---------------")

# ---- RETURN STATEMENT
# Function are even more extensible then they seem. 
# Instead os just printing a value, you can also return a value from a function. 
# This allows you to use the result of a function in other parts of your code, outside of the original function.

#ex:
def add_number(x, y):
    return x + y

result = add_number(4, 4) 
print(result)              #output: 8
print("---------------")

#---

def product(a, b):
    return a * b

print(product(2, 4))  #output: 8
print(product(8, 2))  #output: 16
print(product(4, 8))  #output: 32
print(product(8, 8))  #output: 64
print("---------------")



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
print("---------------")



#-----SCOPE = In this case imagine that is a global scope, meaning a big circle and another smaller circle inside of it. In this big scope you will find n=10 and the smaller you will find the function def print_number. So every time you call inside the smaller circle/code/function you will call n(11) or outside the bigger code you will call n=10. Imagina que o big circle eh avizinhannca e o small circle dentro eh uma casa. e o circulo de dentro decide se vai deixxar alguem entrar caso queira usr algum codigo do circulo maior do lado de fora

n = 10 
print(n)  # Output : 10

def print_number(n):
    print(n)

print_number(11)  #OUTPUT: 11

print(n)          #Output: 10

print("---------------")
#another x:

def add_name(name):
    name = "Hi " + name
    print(name)      #Output: Hi Sthefani

name= "Sthefani"

add_name(name)
print(name)         #Output: Sthefani
print("---------------")


#------ DEFAULT ARGUMENTS
# you can specify default values for the parameters in a function definition. In the code below, we have the parameter name a default value of "world". If we call the funtion without any arguments, the default value will be used. If we call the function with a argument will be used instead.


def greet(name="world"):            #PS: The = iqual sign is important here
    print("Hello, " + name + "!")

greet()                             #Output: "Hello, world!"
greet("Bob")                        #Output: "Hello, Bob!"    
print("---------------")


def greet(greeting="Hello", name="world"):   # This is valid 
    print( greeting + ", " + name + "!")


def greet(greeting, name="world"):           # This is valid as well 
    print( greeting + ", " + name + "!") 


# def greet(greeting="Hello", name):            # This is NOT valid
#     print( greeting + ", " + name + "!")    

print("---------------")



# --- IF STATEMENT
account_balance = -100   # se eu mudar para numero positivo a linha  print("Your account is overdrawn") nao sera printada

if account_balance <0:
        print("Your account is overdrawn") #this print statement belongs to if account_balance, because it indented and follow by :

print("This is always printed.")           # This will alwais be printed  
print("---------------")  

# another ex:
def is_account_balance_low(balance: int) -> None:
    if balance <= 100:
        print("Warning: Low balance.")

is_account_balance_low(99)  # call the function here
is_account_balance_low(100)
is_account_balance_low(101) # this will not be printed
print("---------------")



# ---- IF SCOPE

def pay_bill(balance: int, bill: int) -> int:
    new_balance = balance
    if balance >= bill:
        new_balance = balance - bill
    return new_balance
    
print(pay_bill(100, 30))     #Output: 70
print(pay_bill(100, 100))    #OUtput: 0
print(pay_bill(200, 700))    # here prints the total of the balance 
print("---------------")

# another ex:
def guest_party(invated: int, cancelation: int) -> int:
    total_guest = invated
    if invated >= cancelation:
        total_guest = invated - cancelation
    return total_guest

print(guest_party(10, 8))    #Output: 2
print(guest_party(10, 15))   #Output: 10 aqui no caso seria: se 10 pessoas foram convidadas e 15 cancelou entao total correto de cancelameto foi 10. pois 5 nao existiu ou nunca foram convidados.
print(guest_party(6, 8))     #output: 6
print("---------------")

# ----IF-ELSE STATEMENT 

balance=100
if balance < 0:
    print("account is over")
else:
    print("account is in good standers")
    print("---------------")

 # another exemplo:

def get_min(a: int, b:int) -> int:
    if a < b :
        return a
    else: 
        return b

print(get_min(10, 11))     
print(get_min(5, -7)) 
print(get_min(20, 20))    
print("---------------")

def weather_in_Seattle(cold:int, hot:int) -> int:  #cold:20 < hot:70)
    if cold >= hot:
        return"Today is perfect to drink a hot chocolate and wacth love is blind"
    else:
        return "Go outside, you need to check out the weather, remember to put sun lotion on!"   

print(weather_in_Seattle(10,60))   #Output: Go outside...
print(weather_in_Seattle(20, 19))  #Output: Today is perfect to drink...
print(weather_in_Seattle(20, 25))  #Output: Go outside...  
print("---------------")

# ELSE- IF STATEMEANTS
# we can create of condicional statements using the "elif" keyword(standingfoe else-if)

balance = 1000
def check_balance(balance):
    if balance < 0:
        return " Your account is overdrawn."
    elif balance == 0:
        return "Your account balance is zero." 
    elif balance < 100:
        return "Your account balance is low"
    else:
        return "Your acccount balance is healthy."
        print("---------------")

def check_range(num: int) -> str:
    if num < 0:
        return "negative"
    elif num == 0:
        return "Zero"
    elif num > 0 and num < 10:
        return "Positive single digit"
    else:
        return "Positive multi digit"    

print(check_range(-10))   #Output: negative
print(check_range(0))     #Output: Zero
print(check_range(9))     #Output: Positive single digit
print(check_range(1000))  #Output: Positive multi digit  
print("---------------")

#another ex:
def weather_in_Seattle(cold:int) -> str:
    if cold <= 55:
        return "It is cold today, dont forget your jacket."
    elif cold >= 56 and cold <= 63:
        return "Todays its a perffect day to be outside and exercise. Not too cold and not too hot!"
    elif cold > 64:
        return "Today feels like summer, be ready to drink lots of water and reapply your sun lotion."
print(weather_in_Seattle(10))    
print(weather_in_Seattle(57))    
print(weather_in_Seattle(63))    
print(weather_in_Seattle(90))    
print("---------------")

def weather_in_Seattle(cold: int) -> str:
    if cold <= 55:
        return "It is cold today, don't forget your jacket."
    elif cold <= 63:  # Simplified condition
        return "Today is a perfect day to be outside and exercise. Not too cold and not too hot!"
    else:  # No need for `elif cold > 64`, as it's the only remaining possibility
        return "Today feels like summer, be ready to drink lots of water and reapply your sun lotion."

# Test cases
print(weather_in_Seattle(10))    
print(weather_in_Seattle(57))    
print(weather_in_Seattle(63))    
print(weather_in_Seattle(90))    
print("---------------")


# ----- LOGIC CONDITION
# As we saw earlier we can use the "or", "and", "not" operators to evaluate expressions to execute conditional code blocks.

def discount_applies(age: int) -> bool:
    if age < 18 or age >= 65: #"or"
        return True
    else: 
        return False
print(discount_applies(17))  
print(discount_applies(18))  
print(discount_applies(40))  
print(discount_applies(65))  
print(discount_applies(70))        
print("---------------")


# another ex: Lets say children yonger than 12yo dont pay to entrance and older than 65 also dont pay. Others age pay $25,50 

def ticket_entrance(age: int) -> str:
    if age < 12 or age >= 65:
        return "Your entrance is $0,00 today."
    else:
        return "Your ticket cost $25,50"
    
print(ticket_entrance(13))   #Output: Your ticket cost $25,50
print(ticket_entrance(70))   #Output: Your entrance is 0,00 today.
print(ticket_entrance(35))   #Output: Your ticket cost $25,50
print("---------------")

def ticket_entrance(age: int) -> bool:
    if age < 12 or age >= 65:
        return True
    else:
        return False
    
print(ticket_entrance(13))   #Output: False
print(ticket_entrance(70))   #Output: True
print(ticket_entrance(35))   #Output: False
print("---------------")

#----  WHILE LOOP

i = 0
while i < 5:
    print("I love Python!")
    i = i + 1  # ----->> This line: i = i + 1  is VERY VERY important,
    #this will print only once, 
    #in case i dont have this line, 
    #my code will be a infinite loop (we want to avoid it!!)
    #Output: 
    # I love Python!
    #I love Python!
    #I love Python!
    #I love Python!
    #I love Python!      ## It printed 5x because i = 0    in case it was i=3 the output would be (3x = I love Python! )
    print("---------------")

    # -- another exemplo use the loop exactly 12x:

i = 1
while i < 13:
    print("This loop will run 12 times")
    i = i + 1 #output: it ran 12 time the print statement.
print("---------------")    


# WHILE LOOP COUNTING
# The challenge here is to print number from 0 to 9. Your loop should execute 10 times.

n = 0
while n <= 9:
    print(n)
    n = n + 1

print("---------------")     
    




convidados = 1
while convidados <= 10:
   # print("Convidados estao todos presentes no momento!") 
    print(convidados)
    convidados = convidados + 1
