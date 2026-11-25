#enumerate ->  we can give counter to the collection##############################################################
# names=["roshan","benson","sharief","xavier","mohammad"]
# for i in range(len(names)):
#     print(i,names[i])

# b=list(enumerate(names))
# print(b)

# b=list(enumerate(names,100))
# print(b)

# b=tuple(enumerate(names))
# print(b)

# b=set(enumerate(names))
# print(b)

# b=dict(enumerate(names))
# print(b)

#Anonymous functions(nameless function)#####################################################################
#Anonumous functions are nameless functions and we use a keyword called as "lamda", to create anonymous functions

#write a fucntion to calculate 2*x+5 where x=5
# def f(x):
#     print(2*x+5)
# f(5)
    
# def f():
#     x=int(input("value"))
#     print(2*x+5)
# f()

#syntax
#a=lambaarg:expr
# a=lambda x:2*x+5
# print(a(5))

# a=int(input("a value"))
# b=lambda x:2*x+5
# print(b(a))

# a=int(input("a value"))
# b=int(input("b value"))
# c=lambda a,b: a*b
# print(c(a,b))

# a="CODEGNAN"
# #CODEGNAN
# b=lambda a:a.upper()
# print(b(a))

# b=lambda a:a.upper()
# print(b("codegnan"))

# a="hello python"
# b=lambda a:a.title()
# print(b(a))

# a=input("First name: ")
# b=input("Second name: ")
# c= lambda a,b:(a+' '+b).title()
# print(c(a, b))

# a,b=[x for x in input("names").split(",")]
# c=lambda a,b:(a+" "+b).title()
# print(c(a,b))

# a,b=input("names").split(",")
# c=lambda a,b:(a+" "+b).title()
# print(c(a,b))

#ASCII######################################################################################
#chr(),ord()

# print(chr(65))
# print(chr(23))
# print(chr(90))

# print(ord("a"))
# print(ord("z"))
# #print(ord(97))
# #print(chr("a"))

#a-z,A-Z should be printed
# import string
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

# for i in range(65,91):
#     print((chr(i)),end=" ")
    
# for i in range(97,123):
#     print((chr(i)),end=" ")

name = input("Enter your name: ")
for i in name:
    print(i, ord(i))