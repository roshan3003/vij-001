#math module##########################################################################################################
# import math
# print(math.pi)
# print(math.pi*3)
# print(math.sqrt(2))
# print(math.pow(2,4))
# print(math.tan(45))
# print(math.sin(30))
# print(math.cos(60))
# print(math.log(10))
# print(math.ceil(2.8))
# print(math.floor(5.9))

# import math
# # print(math.round(2.6))
# # print(round(2.8))

# a=5.7890
# print(round(a,2))

# b=6.567890
# print(round(b,1))

# from math import pi,sqrt,log
# print(pi)
# print(sqrt(2))
# print(log(10))
    
#system module######################################################################################################################################
# import sys
# print(sys.path)

# for i in sys.path:
#     print(i)
    
# print(sys.version)

#os module###################################################################################################################################
# import os 
# print(os.path)
# # print(os.listdir())
# # print(os.getcwd())
# # print(os.mkdir("nov28"))
# # print(os.listdir())

# print(os.chdir("C:\\User\\codeg\\Onedrive\\Desktop"))
# print(os.listdir())

#random module###############################################################################################################################
#To generate random number in  python, "randint" function is used.
#This function is defined in random module.
# import random
# a=random.sample(range(10),5)
# print(a)

#randint()###########################################################################################################################
# import random
# a=random.randint(20,25)
# print(a)

#choice()##########################################################################################################################
# import random
# a=[3,4,5,6,7,8,9,10]
# b=random.choice(a)
# print(b)

import random
while True:
    print(" " * 30 + "(Dice code)")
    num=int(input("Enter your dice:"))
    a = random.randint(1, 6)
    print("Dice number is:", a)
    print("Options""\n1.Yes""\n2.No")
    user = int(input("Choose 1 or 2: "))
    if user == 1:
        print("Rolling dice again...")
        continue
    elif user == 2:
        print("Thank you! Game stopped.")
        break
    else:
        print("Invalid choice. Please choose 1 or 2.")
    
        

