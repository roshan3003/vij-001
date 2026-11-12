#list comprehension##############################################################################################
'''a=["codegnan","python","course"]'''
'''a.upper()
print(a)'''

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=",")'''

#every list comprehension can be written as for loop but every for loop cannot be written as list comprehension. 

#syntax###############################################################################
#a=[exp for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

'''a=["hyd","vzg","vja"]
#["Hyd","Vzg","Vja"]
b=[i.title() for i in a]
print(b)'''

'''a=[1,2,3,5,6,7,8,12,13]
#[1,4,9,25,36,49,64,144,169]
b=[i*i for i in a]
b=[i**2 for i in a]
b=[pow(i,2) for i in a]
print(b)'''

#input=16
#output=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15.
'''number=int(input("Enter the number: "))
for i in range(0,number):
    print(i,end=",")'''

'''a=[i for i in range(16)]
print(a)'''

#if usagein comprehemsion
'''number = int(input("Enter the number: "))
for i in range(number):
    if i % 2 == 0:
        print(i,end=",")'''

'''c=int(input("Enter the number: "))
b=[i for i in range(c) if i%2==0]
print(b)'''

'''a=["apple","mango","kiwi","dragon","berry","grapes","banana"]
b=[i for i in a if "a" in i]
print(b)'''

#no-elif usage in list comprehension

'''c=int(input("Enter the number: "))
d=[i*i if i%2==0 else i*5 for i in range(c)]
print(d)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a)) ]
print(c)
