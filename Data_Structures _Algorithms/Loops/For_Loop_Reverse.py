# ---------- FOR LOOPS REVERSE ORDER ---------------
# WE can also use a "for" loop to interate through a sequence of number in reverse order. To do this we can pass a negative number
# ex below:

i = 10
while i > 0:
    print(i)
    i = i - 1

for i in range(10, 0, -1):
    print(i)   
print("-----")     #output: 10 9 8 7 6 5 4 3 2 1

# This is a little bit trick to read. Use the method reverse() may be a simple way to practice
for i in range(20, 9, -1):
    print(i)
print("-----")     #output: 20 19 18 17 16 15 14 13 12 11 10

# EASIER WAY TO SOLVE INSTEAD EX ABOVE:

for i in reversed(range(10)):
    print(i)  
print("-----")     #output: 9 8 7 6 5 4 3 2 1 0

# another ex:
for i in reversed(range(10, 21)):
    print(i)
print("-----")     #output:  20 19 18 17 16 15 14 13 12 11 10  

