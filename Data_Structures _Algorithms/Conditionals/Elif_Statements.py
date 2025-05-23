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
