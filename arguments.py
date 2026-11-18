#* argument ->* is used to unpack the elements
'''a=[2,3,4,5,6]
print(a)
print(*a)

b=(2,3,4,5,6)
print(b)
print(*b)

c={"name":"Balu","age":21}
print(c)
print(*c)'''

'''a="python is language"
print(*a)'''

'''b=[3+6j]
print(*b)'''

'''*a,b,c=1,2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)

a,b,c=1,2,3
print(a)
print(b)
print(c)'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''

#variable length arguments

#variable length arguments are automatically stores in tuple and we use star arguments

'''def check(*a):
    d=2
    for i in a:
        if str(i).isdigit() or str(i).isdecimal():
            d+=i
            print(d)
check(1,2.0,3,4,5,'hi')

def check(*a):
    d=2
    for i in a:
        if type(i) in (float,int):
            d+=i
            print(d)
check(1,2.0,3,4,5,'hi')'''


#splitbill
#test cases
#total frnds- 10                  output
#total amount- 10000               bill is 100

'''def split():
    bill=int(input("Enter the bill amount: "))
    friends=int(input("Enter the number of friends: "))
    final=bill/friends
    print("The bill is",final)
split()'''

'''def splitbill():
    bill=int(input("Enter the bill amount: "))
    friends=int(input("Enter the number of friends: "))
    final=bill/friends
    print("perhead bill is {}".format(final))
    print(f"perhead bill is {final}")
splitbill()'''


    




