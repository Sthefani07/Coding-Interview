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
