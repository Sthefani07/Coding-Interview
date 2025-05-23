# -------- NESTED LOOPS --------
# Suppose we wnat to print all possible pairs from the following set of integers 1 2 3. Where the order of the pairs matters. This would look like :

# 1,1  |  1,2  |  1,3

# 2,1  | 2,2   | 2,3

# 3,1  | 3,2   | 3,3

# This can be accomplished by placing a loop inside of another loop. This is called a nested loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print("-----")     #output:  1,1  |  1,2  |  1,3 | 2,1  | 2,2   | 2,3 | 3,1  | 3,2   | 3,3

#basicamente a primeira fileira se refere ao variable i e a segunda se refere ao variable j. No caso o loop esta printing numbers de 1 - 3 e fazendo todas os possiveis pares
# another ex:

for i in range(3, 6):
    for j in range(3, 6):
        print(i, j)
print("-----")
