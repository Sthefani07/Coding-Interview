# Boolean "OR" = BAsicamente if one of the boolean is true the answer always will be TRUE. 
#         Thuth table
#  |  A        B        A or B    |
#  |  False    False      False   |
#  |  True     False      True    |
#  |  False    True       True    |
#  |  True     True       True    |

a, b, c, d = False, False, True, True

print(a or b)             #output False
print(b or c)             #output True
print(c or d)             #output True
print(a or b or c or d)   #output True
print("-----")

#  BOOLEAN "AND" = Basicamente is TRUE only when they both are TRUE
##         Thuth table
#  |  A        B        A or B    |
#  |  False    False      False   |
#  |  True     False      False   |
#  |  False    True       False   |
#  |  True     True       True    |

a, b, c, d = False, False, True, True

print(a and b)             #output False
print(b and c)             #output False
print(c and d)             #output True
print(a and b and c and d) #output False
print("-----")

# BOOLEAN NEGATION

a = True
b = False
print(not a)          #output: False
print(not b )         #output: True
print(not(a and b))   #output: True
print("-----")
a, b, c = False, False, True
print(not c)           #output: False
print(not(a and b))    #output: True
print(not(b or c))    #output: True used    "or"
print(not(b and c))    #output: False used "and"
print("-----")
