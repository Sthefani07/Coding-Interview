
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