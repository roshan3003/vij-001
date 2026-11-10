#break#################################################################################
'''a=30
while a>1:
    print(a)
    a=a-1
    if a==10:
        break'''

'''a=30
while a>1:
    a=a-1
    if a==20:
        break
    print(a)'''

'''a=30
while a>1:
    a=a-1
    if a==20:
        break
print(a)'''


'''for i in range(15):
    if i==6:
        break
    print(i)'''

'''a="python"
for i in a:
    if i=="o":
        break
    print(a)'''

'''a="python"
for i in a:
    if i=="t":
        break
    print(i)'''


#continue#############################################################################################

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        continue'''
'''a=10
while a>1:
    a=a-1
    if a==5:
        continue
    print(a)'''

'''for i in range(20):
    if i==8:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="t":
     continue
    print(i)#ekkada i este p y t ala print avtundhi 'a' este 4 times print avtundhi full name.'''


#pass########################################################################################
'''a=15
while a>1:
    print(a)
    a=a-1
    if a==6:
        pass#basic ga pass pedithe anni pass yaipotai'''

'''for i in range(25):
    if i==10:
        pass
    print(i)'''


#APPLICATION BUILDING
#ATM
#account-100000
#card="c"  d or e-> invalid card
#pwd=1234->     5678->incorrect password

#insert the card->c
#welcome roshan
#enter the password=1234
#choose the options ->1.bal enq
#                     2.withdrawl    , any other should be invaid
#acc bal is 100000
#enter the amount->20000
#remaining acc bal is -> 80000

Balance=100000
correct_card="amex"
correct_password=1234
username="Roshan"
cardname=input("Enter your card name: ")
if cardname == correct_card:
    print("Welcome",username)
    Pass=int(input("Enter your card password: "))
    if Pass== correct_password:
            option=int(input("Choose the options:\n1.Bal enq\n2.Withdrawl"))
            if option==1:
                print("Account balance available",Balance)
            elif option==2:
                    Withdraw=int(input("Enter the withdrawl amount: "))
                    if Withdraw>Balance:
                        print("Insufficient Balance")
                    else:
                        print("Reaming Balance=",Balance-Withdraw)
            else:
                print("invalid choice")
        






    

