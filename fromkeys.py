#print(dir())

#print(dir("__builtins__"))

#fromkeys()######################################################################################
# a="codegnan"
# print(a)
# print(type(a))

# print(list(a))

# print(tuple(a))

# print(set(a))

# #print(dict(a))
# b=dict.fromkeys(a)
# print(b)

# b=dict.fromkeys(a,"roshan")
# print(b)

# b["d"]="python"
# print(b)

#eval()#####################################################################################################
# while True:
#     a=int(input("a value"))
#     b=int(input("b value"))
#     print(a+b)

# while 1:
#     a=float(input("Enter a value"))
#     b=float(input("Enter b value"))
#     print(a+b)

# while 1:
#     a=input("Enter a value")
#     b=input("Enter b value")
#     print(a+b)

# Now using eval()##############################W
# while 1:
#     a=eval(input("Enter a value"))
#     b=eval(input("Enter b value"))
#     print(a+b)
    
#zip () we can combine multiple collections into one collection####################################################
a=[10,20,30,40,50]
names=["sumanth","gopi","tej","manikanta","uday"]
print(a+names)

b=zip(a,names)
print(b)

# c=list(zip(a,names))
# print(c)

# d=tuple(zip(a,names))
# print(d)

e=set(zip(a,names))
print(e)

f=dict(zip(a,names))
print(f)



