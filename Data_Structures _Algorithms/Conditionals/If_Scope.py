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