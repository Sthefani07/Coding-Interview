
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