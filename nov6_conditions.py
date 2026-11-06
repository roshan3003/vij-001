#if-elif conditions###########################
'''a=3
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=3
b=6
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=3
b=6
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")'''

'''a=10
b=20
if a==b:
    print("equal")
elif a!=b:
    print("not equal")
elif a<b:
    print("less")'''

#USING AND OPERATORS#################################################
'''a=10
b=20
if a ==10 and b ==20:
    print("Both are correct")
elif a ==10 and b!= 20:
    print("Only a is correct")
else:
    print("Both are wrong")'''

#USING OR OPERATOR########################################################
'''a = 10
b = 20
if a ==10 or b ==10:
    print("At least one is 10")
elif a == 20 or b == 20:
    print("At least one is 20")
else:
    print("Neither is 10 or 20")'''

#USING NOT OPERATOR###################################################################
'''a = 10
b = 20
if not a ==b:
    print("not equal")
elif not a < b:
    print("a is greater or equal")
else:
    print("a is less")'''

#bakery
#cakename- price
#redvelvet - 1200
#almond cake - 1000
#chocolate cake - 800
#butterscotch - 600
#remaining cake name -> sorry cake is not available

'''cake=input("Enter cake name: ")
if cake =="redvelvet":
    print("Red Velvet - 1200rs")
elif cake == "almond cake":
    print("Almond Cake - 1000rs")
elif cake == "chocolate cake":
    print("Chocolate Cake - 800rs")
elif cake == "butterscotch":
    print("Butterscotch - 600rs")
else:
    print("Sorry, cake is not available")'''


#price     pizza name
#1000      bbq pizza
#800       crispy chicken pizza
#600       panner pizza
#400       corn pizza
#200       frenchfries & coke

'''price=int(input("Enter the price: "))
if price ==1000:
    print("1000   -   bbq pizza")
elif price == 800:
    print("800   -    crispy chicken pizza")
elif price == 600:
    print("600    -   panner pizza")
elif price== 400:
    print("400    -  corn pizza")
elif price== 200:
    print("200    -   frenchfries & coke")'''

#multiple-if#######################################################################################
'''a=5
b=10
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=5
b=10
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

#multiple-if
#age->18 and above ->eligible for scholarships
#marks->80 and above ->eligible for placements
#attendance->90 and above-> allow to write exams

'''age=int(input("Enter your age: "))
marks=int(input("Enter your marks: "))
attendance=int(input("Enter your attendance : "))
if age>=18:
    print("eligible for scholarships")
else:
    print("not eligible")
if marks>=80:
    print("eligible for placements")
if attendance>=90:
    print("allow to write exams")'''

#positive,negavtive,zero
'''number=int(input("Enter your number: "))
if number==0:
    print("It is zero")
if number <0:
    print("It is negative")
if number>0:
    print("It is positive")'''

#marks>=35->pass
#marks>=60->second class
#marks>=90->distinction
'''marks=int(input("Enter your marks: "))
if marks>=35 and marks<65:
    print("pass")
if marks>=60 and marks<90:
    print("second class")
if marks>=90 and marks<=100:
    print("distinction")'''



    

    
