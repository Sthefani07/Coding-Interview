# ---- FOR LOOP STEPS --------------------
#for loops we can also specify how much we want to increment the variable by on each interaction of the loop. this called the steps.
#Ex below:

i = 0
while i < 10:
    print(i)
    i = i + 2 # this lone prevent the infinit loop + will skip ne the number a cada 2 numeros 2, 4, 6, 8 

for i in range(0, 10, 2):
    print(i)

print("-----")     #output: 0, 2, 4, 6, 8. Da para pensar como se fosse criar uma tabuada

for i in range(0, 110, 10):
    print(i)
print("-----")    