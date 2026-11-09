'''a=[2,4.5,"roshan",7+9j,True,False]
#print the type of all
for i in a:
    print(i)
    print(type(i))'''

#while loop()############################################################################################
'''a=10
while a>1:
    print(a)'''


'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=20
while a>5:
    print(a)
    a+=1'''

'''a=20
while a>=5:
    print(a)
    a-=1'''

'''a=5
while a<100:
    print(a)
    a*=2'''

#range()#########################################################################################################
#start-stop=step
'''or i in range(10):
    print(i,end=" ")#to print in the line and to give space we use end= " "'''

'''for i in range(2,5):
    print(i,end=" ")'''

'''for i in range(2,20,2):
    
    print(i,end=" ")'''

'''for i in range(0,30,3):
    print(i,end=" ")'''

'''for i in range(5,55,5):
    print(i,end=",")'''

#marks          grades
#91 to 101      grade-a
#81 to 91      grade-b
#71 to 81      grade-c
#50 to 71       grade-d
#50 below       grade-e
marks=int(input("Enter your marks:"))
if marks>=91 and marks<=101:
    print("grade-a")
elif marks>=81 and marks<=91:
    print("grade-b")
elif marks>=71 and marks<=81:
    print("grade-c")
elif marks>=50 and marks<=71:
    print("grade-d")
elif marks<50:
    print("grade-e")



    
    



