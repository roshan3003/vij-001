#keyword adn positional arguments######################################################################
'''def Details(id,name,mailid):
    id=10
    name="Roshan"
    mailid="roshan@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="Benson",mailid="b@gmail.com")
Details(id=30,name="Sharief",mailid="s@mailid")
Details(40,"Sonu","o@mailid")
Details("mohammad","m@gmail.com",40)
Details(name="sheema",mailid="h@gmail.com",id=60)'''


#Employee details
#name,designation,salary
'''def Empdetails():
    name=input("Enter your name: ")
    designation=input("Enter your designation: ")
    salary=float(input("Enter your salary: "))
    print("Your details are:- ")
    print(name,designation,salary)
    Empdetails()
Empdetails()'''

'''def Grocery(item,price):
    print("item is %s" %item)
    print("price si %.2f" %price)
Grocery("rice",2000)'''


'''def Grocery(item="sugar",price="100"):
    print("item is %s" %item)
    print("item is %.2f" %price)
Grocery()'''

'''def Grocery(item, price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''

'''def Grocery(item="Ghee",price):
    #non default arg follows default arg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''

#bakery
#cake,price,qty
'''def bakery(cake,price,qty):
    print("Cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %d" %qty)#d is used for integer
bakery("Chocolate",200,2)'''

'''number=int(input("Enter the table you want: "))
for i in range(1,11):
    print(number*i,end=",")'''

userinput=int(input("Enter the table you want: "))
for i in range(1,11):
    print(f"{userinput} x {i} = {userinput*i}")

number=int(input("Enter the table you want: "))
for i in range(1,11):
    print(number,"x",i,"=",number*i)






