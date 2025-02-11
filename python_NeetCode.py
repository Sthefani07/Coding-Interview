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