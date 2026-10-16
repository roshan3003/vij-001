Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=2
print(a)
2
b=5
print(b)
5
x=90
print(x)
90
x=90
print(X)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
z=50
print(z)
50
print(Z)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined. Did you mean: 'z'?
#DONT START A VARIABE WITH A NUMBER
9=20
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a9=20
prit(a9)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    prit(a9)
NameError: name 'prit' is not defined. Did you mean: 'print'?
print(a9)
20
9a=9
SyntaxError: invalid decimal literal
a12345=100
print(a12345)
100
name='roshan'
print(name)
roshan
print('name')
name
city='vja'
print(city)
vja
country = "India"
print(country)
India
#SPECIAL CHARACTERS
@=9
SyntaxError: invalid syntax
$=9
SyntaxError: invalid syntax
_=3
print (_)
3
_a=2
print (_a)
2
 a=60
 
SyntaxError: unexpected indent
#dont start with keywords
if=29
SyntaxError: invalid syntax
else=29
SyntaxError: invalid syntax
int=80
print (int)
80
#multiple variables in single line
a=20,b=29
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a==5,b==34
(False, False)
a=5;b=10
print(a+b)
15
a=19
b=18
print(a+b)
37
a,b=3,5
print(a+b)
8
#single variable multiple values vice versa
a=2,3,4,5,6,
print(a)
(2, 3, 4, 5, 6)
a,b,c=3,4,4,,6,
SyntaxError: invalid syntax
a,b,c=3,4,5,6,7
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a,b,c=3,4,5,6,7
ValueError: too many values to unpack (expected 3, got 5)
a,b,c=(3,4,5)
print(a,b,c)
3 4 5
>>> first name="roshan"
SyntaxError: invalid syntax
>>> first_name="fauzia"
>>> print(first_name)
fauzia
>>> fname="fauzia"
>>> lname=roshan
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    lname=roshan
NameError: name 'roshan' is not defined
>>> fname="fauzia"
>>> lname="roshan"
>>> print(fname+lname)
fauziaroshan
>>> print(fname+" "+lname)
fauzia roshan
>>> print(fname,lname)
fauzia roshan
>>> NAME="ROSHAN"
>>> print(NAME)
ROSHAN
>>> Name="ROSHAN"
>>> print="Name"
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print(Name)
TypeError: 'str' object is not callable
>>> Name="ROSHAN"
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(Name)
TypeError: 'str' object is not callable
>>> a,b,c=100
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a,b,c=100
TypeError: cannot unpack non-iterable int object
>>> a=b=c=100
>>> print(a,b,c)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(a,b,c)
TypeError: 'str' object is not callable
