#kwargs(**)###################################################################################################################
'''def Details(**a):
    print(a)
    print(type(a))
Details()
d={"idnos":[10,20,30],"names":["pavan","balaji","dhanush"],"status":["p","a","p"]}
Details(**d)'''


#return only keys
#return only values
#return both
'''def Details(**a):
    print(a)
    print(type(a))
d={"idnos":[10,20,30],"names":["pavan","balaji","dhanush"],"status":["p","a","p"]}
Details(**d)'''

'''def Details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print([i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
Details()
d={"idnos":[10,20,30],"names":["pavan","balaji","dhanush"],
   "status":["p","a","p"]}
Details(**d)'''


#both * and ** usage
'''def final(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,4.2,3.4)
final(*data)
details={"names":["roshan","appu","sonu"],"city":["vij","hyd","vzg"]}
final(**details)
final(*data,**details)'''

#Railway ticket
#ticket=1000
#gender->male
#>60->seniot citizen->flat-30%->700
#<60-> normal citizen->no dis->1000

#female
#>60->senior citizen->flat-50%->500
#<60->normal citizen->flat-30%->700
while True:
    print("RAILWAY TICKET")
    def ticket():
        ticket = 1000
        gender = input("Enter your gender: ").lower()
        age = int(input("Enter your age: "))
        if gender == "male" and age < 60:
            print("Your ticket price is",ticekt)
        elif gender == "male" and age >= 60:
            print("Your ticket price is",int(ticket-(ticket*0.30)))
        elif gender == "female" and age < 60:
            print("Your ticket price is",int(ticket-(ticket*0.30)))
        elif gender == "female" and age >= 60:
            print("Your ticket price is",int(ticket-(ticket*0.50)))
        else:
            print("Invalid input")
    ticket()
        


