#nested-if#####################################################################
'''a=3
b=7
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=3
b=7
if a==b:
    print("less")
    if b>a:
        print("greater")'''

'''a=5
b=10
if a!=b:
    print("not equal")
    if a==b:
        print("equal")'''

'''a=4
b=8
if a<b:
    print("less")
    if a>b:
        print("greater")
    else:
        print("true")'''

'''a=4
b=8
if a==b:
    print("less")
    if a>b:
        print("greater")
    else:
        print("true")
else:
    print("false")'''


'''a=4
b=8
if a<b:
    print("less")
    if a>b:
        print("false")
    elif b>a:
        print("greater")
    else:
        print("true")'''

#social media login
#username->roshan
#password->1234
#match->login succesful
#notmatch->invalid credentials

'''print("Social Media Login")
username = input("Enter username: ")
if username == "roshan":
    password = input("Enter password: ")
    if password == "1234":
        print("Login successful")
    else:
        print("Invalid credentials")
else:
    print("User name not found")'''

#loops
#for(),while(),rage(),break(),continue(),pass()
#for()
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''b=(5,6,7,8,9,10)
for i in b:
    print(i)
print(type(b))
print(type(i))'''

'''c={5,6,7,8,9}
for i in c:
    print(i)
print(type(c))
print(type(i))'''

'''a={"name":"roshan","year":2026,"month":11}
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[2.3,4.5,6.7]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=["roshan","year","month"]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[6+9j,4+7j]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[True,False]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[2,3.4,"Roshan",9+6j,True]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

a=["apple","banana","grapes"]
#["APPLE","BANANA","GRAPES"]
for i in a:
    print(i.upper())











