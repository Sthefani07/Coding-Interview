#-----SCOPE = In this case imagine that is a global scope, meaning a big circle and another smaller circle inside of it. In this big scope you will find n=10 and the smaller you will find the function def print_number. So every time you call inside the smaller circle/code/function you will call n(11) or outside the bigger code you will call n=10. Imagina que o big circle eh avizinhannca e o small circle dentro eh uma casa. e o circulo de dentro decide se vai deixxar alguem entrar caso queira usr algum codigo do circulo maior do lado de fora

n = 10 
print(n)  # Output : 10

def print_number(n):
    print(n)

print_number(11)  #OUTPUT: 11

print(n)          #Output: 10

print("-----")
#another x:

def add_name(name):
    name = "Hi " + name
    print(name)      #Output: Hi Sthefani

name= "Sthefani"

add_name(name)
print(name)         #Output: Sthefani
print("-----")