def lastWordLength(s: str) -> int:
    word = s.split()                     #split the string into words

    last_word= word[-1]                  #get the last word   
    return last_word, len(last_word)     #return the last word and the length

    #return len(word[-1])               #returning the length of the last word (only) 


print(lastWordLength("Hey amor te amo"))
print(lastWordLength("This is fun"))