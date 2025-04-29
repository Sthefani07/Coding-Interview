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
print("-----")

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
print("-----") 

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
print("-----") 

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
print("-----") 

# Another challenge is reassing the variable to print a integer / numero inteiro
pi = 3.748798759
square_root_8 = 2.759874
#  code below
pi = int(pi)
square_root_8 = int(square_root_8)

print(pi)
print(square_root_8)
print("-----") 

# Eu posso converter uma sting (numero) para integer da forma feita abaixo
variable = "10" 
print(type(variable))

variable = int(variable)
print(type(variable))
print("-----") 

# Arithmetic Operators

x , y = 3, 6

print(x + y)    # Output : 9    integer 
print(x - y)    # Output : -3
print(x * y)    # Output : 18
print(x / y)    # Output : 0.5  float number
variable = int(variable)
print(type(variable))
print("-----") 

## Exercise 
a, b, c = 2, 2, 0.5

total_sum = a + b + c # giving a name to the variable
total_product = a * b * c

print(total_sum)
print(0 - total_sum)
print(a * b * c)
print(total_sum / total_product)
print("-----") 

# MORE OPERATORS
        # Floor division : //
        # Modulus : %
        # Exponentiation : **

# Here is a exemplo:
x, y = 7, 2  

print(x // y) # Output : 3 ( 7 divided by 2 is 3.5, after rounding donw we get 3)
print(x % y)  # Output : 1 (7 divided by 2 is 3, with a remainder of 1)
print(x ** y) # Output : 49 (7 raised to the power of 2 is 49, 7*7 = 49)
print("-----") 

## Exercise 
 
a, b, c = 2, 8, 5

product_a_b = a * b
print(product_a_b // c)
print(product_a_b % c)
print(a ** b)
print(b ** c)
print("-----")

# Shorthand Operator
count = 0
count = count + 1
count = count + 2
print(count)  # Output : 3
print("-----")

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
print("-----")

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
print("-----")

# BOOLEAN NEGATION

a = True
b = False
print(not a)          #output: False
print(not b )         #output: True
print(not(a and b))   #output: True
print("-----")
a, b, c = False, False, True
print(not c)           #output: False
print(not(a and b))    #output: True
print(not(b or c))    #output: True used    "or"
print(not(b and c))    #output: False used "and"
print("-----")

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



#-----SCOPE = In this case imagine that is a global scope, meaning a big circle and another smaller circle inside of it. In this big scope you will find n=10 and the smaller you will find the function def print_number. So every time you call inside the smaller circle/code/function you will call n(11) or outside the bigger code you will call n=10. Imagina que o big circle eh avizinhannca e o small circle dentro eh uma casa. e o circulo de dentro decide se vai deixxar alguem entrar caso queira usr algum codigo do circulo maior do lado de fora

n = 10 
print(n)  # Output : 10

def print_number(n):
    print(n)

print_number(11)  #OUTPUT: 11

print(n)          #Output: 10

print("-----")
#another x:

def add_name(name):
    name = "Hi " + name
    print(name)      #Output: Hi Sthefani

name= "Sthefani"

add_name(name)
print(name)         #Output: Sthefani
print("-----")


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



# --- IF STATEMENT
account_balance = -100   # se eu mudar para numero positivo a linha  print("Your account is overdrawn") nao sera printada

if account_balance <0:
        print("Your account is overdrawn") #this print statement belongs to if account_balance, because it indented and follow by :

print("This is always printed.")           # This will alwais be printed  
print("-----")  

# another ex:
def is_account_balance_low(balance: int) -> None:
    if balance <= 100:
        print("Warning: Low balance.")

is_account_balance_low(99)  # call the function here
is_account_balance_low(100)
is_account_balance_low(101) # this will not be printed
print("-----")



# ---- IF SCOPE

def pay_bill(balance: int, bill: int) -> int:
    new_balance = balance
    if balance >= bill:
        new_balance = balance - bill
    return new_balance
    
print(pay_bill(100, 30))     #Output: 70
print(pay_bill(100, 100))    #OUtput: 0
print(pay_bill(200, 700))    # here prints the total of the balance 
print("-----")

# another ex:
def guest_party(invated: int, cancelation: int) -> int:
    total_guest = invated
    if invated >= cancelation:
        total_guest = invated - cancelation
    return total_guest

print(guest_party(10, 8))    #Output: 2
print(guest_party(10, 15))   #Output: 10 aqui no caso seria: se 10 pessoas foram convidadas e 15 cancelou entao total correto de cancelameto foi 10. pois 5 nao existiu ou nunca foram convidados.
print(guest_party(6, 8))     #output: 6
print("-----")

# ----IF-ELSE STATEMENT 

balance=100
if balance < 0:
    print("account is over")
else:
    print("account is in good standers")
    print("-----")

 # another exemplo:

def get_min(a: int, b:int) -> int:
    if a < b :
        return a
    else: 
        return b

print(get_min(10, 11))     
print(get_min(5, -7)) 
print(get_min(20, 20))    
print("-----")

def weather_in_Seattle(cold:int, hot:int) -> int:  #cold:20 < hot:70)
    if cold >= hot:
        return"Today is perfect to drink a hot chocolate and wacth love is blind"
    else:
        return "Go outside, you need to check out the weather, remember to put sun lotion on!"   

print(weather_in_Seattle(10,60))   #Output: Go outside...
print(weather_in_Seattle(20, 19))  #Output: Today is perfect to drink...
print(weather_in_Seattle(20, 25))  #Output: Go outside...  
print("-----")

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
        print("-----")

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
print("-----")

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
print("-----")

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
print("-----")


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
print("-----")


# another ex: Lets say children yonger than 12yo dont pay to entrance and older than 65 also dont pay. Others age pay $25,50 

def ticket_entrance(age: int) -> str:
    if age < 12 or age >= 65:
        return "Your entrance is $0,00 today."
    else:
        return "Your ticket cost $25,50"
    
print(ticket_entrance(13))   #Output: Your ticket cost $25,50
print(ticket_entrance(70))   #Output: Your entrance is 0,00 today.
print(ticket_entrance(35))   #Output: Your ticket cost $25,50
print("-----")

def ticket_entrance(age: int) -> bool:
    if age < 12 or age >= 65:
        return True
    else:
        return False
    
print(ticket_entrance(13))   #Output: False
print(ticket_entrance(70))   #Output: True
print(ticket_entrance(35))   #Output: False
print("-----")

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
    print("-----")

    # -- another exemplo use the loop exactly 12x:

i = 1
while i < 13:
    print("This loop will run 12 times")
    i = i + 1 #output: it ran 12 time the print statement.
print("-----")    


# WHILE LOOP COUNTING
# The challenge here is to print number from 0 to 9. Your loop should execute 10 times.

n = 0
while n <= 9:
    print(n)
    n = n + 1

print("-----")     
    

convidados = 1
while convidados <= 10:
   # print("Convidados estao todos presentes no momento!") 
    print(convidados)
    convidados = convidados + 1
print("-----")      


# WHILE LOOP MULLTIPLES
n = 10
while n <= 90:               # prestar atencao no simbolo de > ou < pois estava fazendo confusao com eles e afetando drasticamento no resultado
    print(n)
    n = n + 10
print("-----")      #output: 10, 20, 30, 40, 50, 60, .... 90


# ------ FOR LOOPS -------------
# The loop starts with a key word "for". 1- Next you need to specify the variable name, This variable will represent each item in the sequence. 3- After the varible name, you need to use the keyword "in". 4- Finally, you need to specify the sequence you want to iterate over. for exemple function = range(10). This function generates a sequence of numbers from 0 to 9. 10 is not included in the sequence.

for num in range(13):
    print(num)    
print("-----")   #output: 0 1 2 3 4 5 6 7 8 9 10 11 12

# ---------- FOR LOOPS START -----------
# If you want your for loop starting at a different number you can simply pass two arguments in to the range() function

i = 2
while i < 5:
    print(i)
    i = i + 1 # line to prevente a infinit loop

#--ex of the same result in a for loop below

for i in range(2, 5):
    print(i)

print("-----")     #output: 2 3 4

for i in range(10, 21):
    print(i)

print("-----")


# ---- FOR LOOP STEPS --------------------
#for loops we can also specify how much we want to increment the variable by on each interaction of the loop. this called the steps.
#Ex below:

i = 0
while i < 10:
    print(i)
    i = i + 2 # this lone prevent the infinit loop + will skip ne the number a cada 2 numeros 2, 4, 6, 8 

for i in range(0, 10, 2):
    print(i)

print("-----")     #output: 0, 2, 4, 6, 8. Da para pensar como se fosse criar uma tabuada

for i in range(0, 110, 10):
    print(i)
print("-----")    

# ---------- FOR LOOPS REVERSE ORDER ---------------
# WE can also use a "for" loop to interate through a sequence of number in reverse order. To do this we can pass a negative number
# ex below:

i = 10
while i > 0:
    print(i)
    i = i - 1

for i in range(10, 0, -1):
    print(i)   
print("-----")     #output: 10 9 8 7 6 5 4 3 2 1

# This is a little bit trick to read. Use the method reverse() may be a simple way to practice
for i in range(20, 9, -1):
    print(i)
print("-----")     #output: 20 19 18 17 16 15 14 13 12 11 10

# EASIER WAY TO SOLVE INSTEAD EX ABOVE:

for i in reversed(range(10)):
    print(i)  
print("-----")     #output: 9 8 7 6 5 4 3 2 1 0

# another ex:
for i in reversed(range(10, 21)):
    print(i)
print("-----")     #output:  20 19 18 17 16 15 14 13 12 11 10  


# -------- NESTED LOOPS --------
# Suppose we wnat to print all possible pairs from the following set of integers 1 2 3. Where the order of the pairs matters. This would look like :

# 1,1  |  1,2  |  1,3

# 2,1  | 2,2   | 2,3

# 3,1  | 3,2   | 3,3

# This can be accomplished by placing a loop inside of another loop. This is called a nested loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print("-----")     #output:  1,1  |  1,2  |  1,3 | 2,1  | 2,2   | 2,3 | 3,1  | 3,2   | 3,3

#basicamente a primeira fileira se refere ao variable i e a segunda se refere ao variable j. No caso o loop esta printing numbers de 1 - 3 e fazendo todas os possiveis pares
# another ex:

for i in range(3, 6):
    for j in range(3, 6):
        print(i, j)
print("-----")


# ----------Control Flow ------------
# Key words 
# "Break" exits the loop immediately 
# "continue": Skips the remaining code inside the loop for the current iteration and moves to the next iteration. 
# "pass": Acts as a placeholder and does nothing

for i in range(1, 8):
    pass

if True:
    pass

def test_function():
    pass

for i in range(1, 8):
    break


#another ex:

for i in range(1, 8):
    if i == 3:  
        continue
    elif i == 6:
        break
    print(i)
print("-----")

# ----------- LENGTH FUNCTION ----------
# Suppose we had a string like: my_str = "Jaboticaba" and we wanted to know how many characters are in the string. We can use a built in function called: len() to find the length of a string(and many other data types)

my_str = "Jaboticaba"
print(len(my_str)) #output: 10
print("-----")

# another ex:
def get_longer_word(word1: str, word2: str) -> str:
    if len(word1) >= len(word2): # nessa linha o sinal de " = " eh importante
        return word1
    else:
        return word2



print(get_longer_word("yellow", "red"))
print(get_longer_word("red", "blue"))    
print(get_longer_word("green", "yellow")) 
print("-----")

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

# ----------- STRING LOOP SHORTHAND ------------------
# Consider thhe following code: 

my_string = "Hello"

for i in range(len(my_string)):
    print(i, my_string[i])     # para ter o numero tbm printed, apenas adicionar o "i," 
print("-----")

# another ex:


def print_string_characters(word1: str, word2:str) -> None:
    for c in word1:
        print(c)
    for c in word2:
        print(c)


print_string_characters("Hello,World!","Good Job!")
print("-----")


# ---------- STRING CONCATENATION --------------
# CONCATINATION IS A PROCESS OS COMBINING TWO OR MORE STRINGS into a single using "+"

def concatenate(s1: str, s2: str) -> str:
    s3 = s1 + s2
    if len(s3) > 10:
        return "Too long!"
    return s3


print(concatenate("He", "llo"))
print(concatenate("Hello", "world!"))
print(concatenate("Length", "of10"))
print("-----")


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


# ----------------------- REVERSING A STRING ----------------------------
# We can also slicing to reverse a string. By not specifying the starting of the index or the ending index, and setting the step to -1, the string will be reversed.

my_string = "Hello"

print(my_string[::-1]) # output: olleH
print("-----")

#another ex:

my_string = "Hello"
start, end, step = 1, 4, 1

#print(my_string[start:end])       # output: ello

print(my_string[start:end:-1])   # output: lle

#another ex:

def reverse_string(input_string:str) -> str:
    return input_string[::-1]

print(reverse_string("Seattle"))   # output: elttaeS
print(reverse_string("Sthefani"))  # output: inafehtS
print(reverse_string("Hello"))     # output: olleH
print("-----")


# ----------------------- STRINGS ARE IMMUTABLE ----------------------------

# it's important to know that whenever you slice a string, you are not modifying the underlying string. Instead, you are creating a new string with the sliced characters. This is because strings are immutable in Python, which means they cannot be changed after they are created.

message = "I will never change."

#message[0] = "x" # This will cause a error

# In the code above, we cannot change individual characters, we can only reassing the entire srting.
 
 # another ex:

message = "I will never change."

before_second = message[:1] # "I"
after_second = message[2:]  #"Will never change."

new_message = before_second + after_second
print(new_message)
print("-----")

#another ex:

def remove_fourth_character(word:str) -> str: #we will remove the fourth index
    first_part = word[:3]
    second_part= word[4:]
    return first_part + second_part


print(remove_fourth_character("Seattle"))
print(remove_fourth_character("Bellevue"))
print("-----")


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


# ----------------------- INTRO TO LIST ----------------------------

#In Python a list is a collection of items that are stored in a specific order.

my_list = [1, 2, 3]

print(len(my_list))  #output: 3
print(my_list[0])    #output: 1
print(my_list[1])    #output: 2
print(my_list[2])    #output: 3

# A difference between list and strings. List are mutable, meaning we can change the value of the elementd in the lists.

my_list = [1, 2, 3, 4, 5]

my_list[0] = 10

print(my_list[0])  # Output: 10

# another ex:

my_list = ["I", "am", "a", "list"]

print(my_list[0]) #output: I
print(my_list[1]) #Output: am
print(my_list[2]) #Output: a
print(my_list[3]) #Output: list


# another exemplo:

my_list = [1, 7, 5, 4, 3, 2]

print(my_list[1])
print(my_list[2])
print(my_list[0])
print(len(my_list))  #Output: 6



# ----------------------- LIST OPERATOR ----------------------------

#List can also be used within conditional statements. For example, we can check if a list is empty or not:

my_list = [1, 2, 3]

if len(my_list) > 0:
    print("The list is not empty")

else:
    print("THe list is empty.")

# We can also use the "in" operator to check if an element is present in a list:


my_list = [1, 2, 3]

if 2 in my_list:  # if 2 is in my list, then do .... 
    print("2 is in the list")
else:
    print("2 is not in the list")    

#another ex: ------

def check_list_empty(my_list) -> bool:
    if len(my_list) == 0:
        return True
    return False

#or the same example below in a shorter version:
def check_list_empty(my_list) -> bool:
    return len(my_list) == 0 
print("-----")

#another ex: ------
def check_element_in_list(my_list, element) -> bool:
    if element in my_list:
        return True
    return False

#or the same example below in a shorter version:
def check_element_in_list(my_list, element) -> bool:
    return element in my_list


print(check_list_empty([]))
print(check_list_empty([1, 2, 3]))

print(check_element_in_list([1,2, 3], 1))
print(check_element_in_list([1, 2, 3], 4))
print("-----")

# ----------------------- LIST LOOPING ----------------------------

# We can also loop through lists similar t how we loop through strings:

# By using the length of the list:
my_list = [1, 2, 3, 4, 5]

length = len(my_list)

for i in range(length):
    print(my_list[i])
print("-----")     # Output: 1 2 3 4 5 

    # Or by using the "in" operator :

my_list = [1, 2, 3, 4, 5]  

for element in my_list:
    print(element)
print("-----")  # Output: 1 2 3 4 5 

#another ex: how many times does x appear in this input?

from typing import List # used to add type hint for list

def count_x(nums: List[int], x: int) -> int:
    result= 0
    for n in nums:
        if n == x:
            result = result + 1
    return result        

print(count_x([1, 2, 5, 6, 5], 5))    #output: 2
print(count_x([4, 3, 6, 1, 6], 5))    #output: 0
print(count_x([4, 7, 7, 6, 7, 6], 7)) #output: 3
print("-----")


# ----------------------- LIST FUNCTIONS ----------------------------

# Python also provides some built in functions to get the sum, minimum, and maximum of a list:

my_list = [1, 2, 3, 4, 5]

print(sum(my_list)) #Output: 15
print(min(my_list)) #Output: 1
print(max(my_list)) #Output: 5
print("-----")

# 1* The sum() funtion returns the sum of all the elements in the list
# 2* The min() function returns the smallest element in the list.
# 3* The max() function returns the largest element in the list.

#another ex:

from typing import List

def get_sum(my_list: List[int]) -> int:
    total = 0
    for n in my_list:
        total += n 
    return total

def get_min(my_list: List[int]) -> int:
    min_num = my_list[0]
    for n in my_list:
        if n < min_num:
            min_num = n
    return min_num

def get_max(my_list: List[int]) -> int:
    max_num = my_list[0]
    for n in my_list:
        if n > max_num:
            max_num = n
    return max_num


print(get_sum([1, 2, 3, 4, 5]))  #Output: 15
print(get_sum([5, 4, 5, 6]))     #Output: 20
print("-----")
print(get_min([7, 3, 4, 5]))     #Output: 3
print(get_min([5, 4, 5, 6]))     #Output: 4
print("-----")
print(get_max([7, 3, 4, 5]))     #Output: 7
print(get_max([7, 9, 4, 1]))     #Output: 9
print("-----")


# ----------------------- LIST APPEND ----------------------------

# We can do more than just change individual elements within a list. We can also add new element to the end of the list using the append() function.

my_list = [1, 2, 3]
print(my_list) #output: [1,2,3]

my_list.append(4)
print(my_list) # Output: [1,2,3,4]
print("-----")

# A few thing to notice:

# 1* We can print an a entire list at once.

# 2* The append() function adds an element to the end to the list. This is not a separate function, it's called with a period after the list name (append()). This is called a method. It is a function that is associated with a specific object(in this case a list is an object). 

# 3* After calling append, the original list has been modified to include the new element at the end. The length increased from 3 to 4.


#ex: It should append(add to the end of the list) each number from elements to the end of the my_list and return the modified list.

from typing import List

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:

    for n in elements:
        my_list.append(n)
    return my_list

print(append_to_list([1, 2, 3], [4, 5])) #Output: [1, 2, 3, 4, 5]
print(append_to_list([], [1, 2, 3, 4]))  #Output: [1, 2, 3, 4]
print("-----")
