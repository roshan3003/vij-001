#functions################################################################################################################
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(9,22)'''

#//,**,%
'''def calculate(a,b):
    print("the floor division is",a//b)
    print("the pow is",a**b)
    print("the remainder is",a%b)
calculate(9,22)
calculate(100,222)'''

'''while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    cal()'''

'''def cal():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    cal()# if we keep the def here it will work as while loop
cal()'''

'''def fullname():
    fname=input("Enter your first name: ")
    lname=input("Enter your last name: ")
    print((fname+" "+lname).title())
    fullname()
fullname()'''

#print v/s return
#Print:- Print just shows the human user output in a console.
#Return:- Return will terminate the function and gives back a value from the function.

'''def mul(a,b):
    print(a*b)
mul(2,5)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,3)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #retunr d
    #return e
    return c,d,e
print(cal(3,4))'''

'''def cal():
    a=int(input("Enter the a: "))
    b=int(input("Enter the b: "))
    return a+b
print(cal())'''

#enter the value ->7###############################################################################################################
#b value->9
#options->1.add
#2.sub
#3.mul

'''def cal():
    a=int(input("Enter the a value: "))
    b=int(input("Enter the b value: "))
    option=int(input("Choose the option:\n1.Add\n2.Subtarct\n3.Multiply"))
    if  option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    else:
        print(a*b)
    cal()
cal()'''


'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
        a=int(input("Enter the a value: "))
        b=int(input("Enter the b value: "))
        option=int(input("Choose the option:\n1.Add\n2.Subtarct\n3.Multiply"))
        if  option==1:
         add()
        elif option==2:
         sub()
        else:
         mul()'''
        
   
    
                




    
    







