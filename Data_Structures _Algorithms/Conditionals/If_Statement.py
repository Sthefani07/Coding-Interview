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
