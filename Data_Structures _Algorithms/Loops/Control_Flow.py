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
