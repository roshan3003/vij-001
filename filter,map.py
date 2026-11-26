#filter()######################################################################################################
# a=[2,4,5,7,8,10,12,14,16,25,30,100]
# # # if a%2==0:
# # #     print(a)
# # for i in a:
# #     if i%2==0:
# #         print(i)
        
# b=list(filter(lambda i:i%2==0,a))
# print(b)

#[],(),{}######################################################################################################
# a=[]
# print(type(a))

# b=()
# print(type(b))

# c=set()
# print(type(c))

# d={}
# print(type(d))

# a=[[],(),set(),{}," ",None,2,5.6,"python",7+9j,True,False]
# b=list(filter([],a))#this wont work until u keep- list(filter(None,a))
# print(b)

#map()-> each object from a collection and forms a new collection#######################################################
# a=[2,5,7,10,20,40,60]
# b=[1,3,4,11,15,35,70]
# c=list(map(max,a,b))
# print(c)
# d=list(map(min,a,b))
# print(d)

# print(ord('+'))

# a=["c","c++","ml","java","python"]
# b=["html","css","js","bs","react"]
# c=list(map(max,a,b))
# print(c)
# d=list(map(min,a,b))
# print(d)

# a=input("data1")
# b=input("data2")
# print(a+b)

# a,b=input("data").split(",")
# print(a+b)

# a,b=(x for x in input("enter the names: ").split(","))
# print(a+b)

#int###################################################################################################################
# a=int(input("a value: "))
# b=int(input("b value: "))
# print(a+b)

# a,b=int(input("values").split(","))
# print(a+b)#error

# a,b=(int(x) for x in input("enter the value").split(","))
# print(a+b)

# a,b=[int(x) for x in input("enter the value").split(",")]
# print(a+b)

# a,b=map(int,input("enter the values").split(","))
# print(a+b)

# a=list(map(int, input("enter the values").split(",")))
# print(a)

# a=tuple(map(int, input("enter the values").split(",")))
# print(a)

# a=set(map(int, input("enter the values").split(",")))
# print(a)