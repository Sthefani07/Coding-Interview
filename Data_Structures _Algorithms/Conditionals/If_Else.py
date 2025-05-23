#  IF_ELSE STATEMENT 

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