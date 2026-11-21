#global and local variables
#a variable defined inside and outside the function are called global and local variables
#a variable is defined outside the function it is considerd as a entire global space is
#called global variable and inside the function is called local variable
#First5 case of global variable
'''a=2
def check1():
    print("inside value is", a)
check1()
print("outside value is", a)'''

#second case of global variable

'''a=4
def check2():
    a=5
    a=a**2
    print("inside value is", a)
check2()
print("outside value is", a+5)'''

#third case of global variable and local variable
'''a=3
b=9
def check3():
    a=6
    print("inside value is", a)
    a=7
    print("updated value is", a+5)
    b=12#local variable
    b=b+a
    print("value of b", b)
check3()
print("a value is", a)
print("b value is", b)'''

#usage of global keyword
#when user want to create a variable inside the function directly and carry forward the updated value even outside the
#function then we need to use global keyword.

a=10
def final():
    global a
    print("inside value is",a)
    a=15
    print("updated value is",a)
    global b
    b=20
    b=b+a
    print("Value of b",b)
final() 
print("value of a",a)
print("b value is ",b)

