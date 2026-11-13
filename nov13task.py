'''attend tracker
no of student->5

stu1-p
stu2-q
stu3-p
stu4-a
stu5-p
 run time ask about student
 no of students->5
 rember of persent ->3
 no of absent-2'''
#using WHILE####################################################################################

print("ATTENDANCE TRACKER")
totstud=int(input("Enter the number of students: "))
present=0
absent=0
i=1
while True:
    print("Student: ",i)
    check=input("")
    if check=="p":
        present+=1
    else:
        absent+=1
    if i==totstud:
        break
    i+=1
print("No of students= ",totstud)
print("No of sudents present=",present)
print("No of sudents absent=",absent)


#USING FOR############################################################################################
print("ATTENDANCE TRACKER")
totstud=int(input("Enter the number of students: "))
present=0
absent=0
for i in range(1,totstud+1):
    print("Student: ",i)
    check=input("")
    if check=="p":
        present+=1
    else:
        absent+=1
print("No of students= ",totstud)
print("No of sudents present=",present)
print("No of sudents absent=",absent)



    

    
    
    

    
