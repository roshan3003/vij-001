#if-else conditions by using logical operators#######################
'''a=4
b=8
if a<b and b>a:
    print("less")
else:
    print("greater")'''

#if-else conditions by using identify operators########################
'''a=6.7
if type(a)is float:
    print("true")
else:
    print("false")'''

#if-else conditions by using membership operators###########################
'''a=[3,4,5,6,7,8,9,10]
if 10 in a:
    print("true")
else:
    print("false")'''

#voting
'''age=int(input("enter the age"))
if age>18:
    print("eligible for vote")
else:
    print("Not eligible for vote")'''

#even or odd
'''num = int(input("Enter a number: "))
if num % 2 == 0:
    print("It is Even")
else:
    print("It is Odd")'''

#leap year
'''year = int(input("Enter a year: "))
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")'''

#guest
'''name=input("Enter your name: ")
if name== "Roshan":
    print("Welcome",name)
else:
    print("Welcome Guest")'''

#guest for 5 people
'''names = ["Roshan", "Sonu", "Fauzia", "Sheema", "Sharief"]
h = input("Enter your name: ").capitalize()
if h in names:
    print("Welcome", h)
else:
    print("Welcome Guest")'''

#vowels consonants for 5 people
letter = ["a", "e", "i", "o", "u"]
h = input("Enter your letter: ")
if h in letter:
    print("It is Vowel")
else:
    print("It is Consonant")
