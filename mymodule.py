# def greeting (name):
#     print("Welcome",name)

# a=3
# b=6
# print("the sum is",a+b)

# fname=input("first name")
# lname=input("last name")
# print(fname+" "+lname)

# details = {"names":["harsha","Sai","Pooja"],"marks":[70,80,90]}

if __name__=="__main__":
    a=[10,20,30,40,50]
    #a.append("code") this will add the as single word but we want single single letter
    a.extend("code")#so we use this
    print(a)
    
def dummy():
    if __name__=="__main__":
        print("this program is run as script ")
    else:
        print("this program is run as module")
dummy()
    