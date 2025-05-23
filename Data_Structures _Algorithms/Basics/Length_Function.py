# ----------- LENGTH FUNCTION ----------
# Suppose we had a string like: my_str = "Jaboticaba" and we wanted to know how many characters are in the string. We can use a built in function called: len() to find the length of a string(and many other data types)

my_str = "Jaboticaba"
print(len(my_str)) #output: 10
print("-----")

# another ex:
def get_longer_word(word1: str, word2: str) -> str:
    if len(word1) >= len(word2): # nessa linha o sinal de " = " eh importante
        return word1
    else:
        return word2



print(get_longer_word("yellow", "red"))
print(get_longer_word("red", "blue"))    
print(get_longer_word("green", "yellow")) 
print("-----")
