Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=b=c=100
>>> print(a,b,c)
100 100 100
>>> a=10
>>> print(a)
10
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
#datatypes
a=10
type(a)
