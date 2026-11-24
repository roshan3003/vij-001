#generators
#no tuple comprehensions in above cases if we remove those braces"[]" and keep paranthesis "()" then the outcome is generator.
#syntax
#a=[expr for var in collection/range]
'''a=(i for i in range(16))
print(a)
print(*a)
print(type(a))'''

#print(list(a))
#print(tuple(a))
#print(set(a))

# A generator is also a function which can be used as an iterator (Loop) by producing group of values, where we can use yield

#YIED VS RETURN
#Return will terminate the function where as yield can pass the function and go on with every succesive iteration
'''a,b=[int(x) for x in input("enter the values: ").split(",")]
print(a+b)'''

'''`a,b=[int(x) for x in input("enter the values: ").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
check(a,b)'''

'''a,b=[int(x) for x in input("enter the values: ").split(",")]
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
check(a,b)'''

'''a,b=[int(x) for x in input("enter the values: ").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''

#yield V/S return

'''def mygen():
    #return "python"
    #return "java"
    #return "ds"
    return "python","java","ds"
print(*mygen())'''

'''def mygen():
    yield "vja"
    yield "hyd"
    yield "vzg"
print(*mygen())'''

#next() #one by one iteration
'''d=mygen()
print(next(d))
print(next(d))
print(next(d))'''

#max(), min(), sum()

print(max(2,4,7,9,11,15,30))
#min()
print(min(3,4,5,6,7))

#print(sum(3,4))
a=2,3,4,5,6,7,8,9,10
print(sum(a))
#sum withouy variable
print(sum([1,2,3,4,5,6]))


