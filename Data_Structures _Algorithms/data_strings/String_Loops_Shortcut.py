# ----------- STRING LOOP SHORTHAND ------------------
# Consider thhe following code: 

my_string = "Hello"

for i in range(len(my_string)):
    print(i, my_string[i])     # para ter o numero tbm printed, apenas adicionar o "i," 
print("-----")

# another ex:


def print_string_characters(word1: str, word2:str) -> None:
    for c in word1:
        print(c)
    for c in word2:
        print(c)


print_string_characters("Hello,World!","Good Job!")
print("-----")

