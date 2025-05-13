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
