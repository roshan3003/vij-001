Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#logical
a=3
b=6
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a
3
,
a<b or b>a
True
a>b or b>a
True
a!=b or a==b
True
a<=b or b>=a
True
not True
False
not False
True

#identify
a=3
type(a) is int
True
type(a) is not int
False
type(a) is float
False
type(a) is not float
True
type(a) is complex
False
type(a) is not complex
True
type(a) is str
False
type(a) is not str
True
type(a) is bool
False
type(a) is not bool
True
a='pyhton'
type(a) is str
True
type(a) is not str
False

#membership
a=1,2,3,4,5,6,7,8,9
9 in a
True
10 in a
False
10 not in a
True

#Bitwise
a=4
>>> b=8
>>> a|b
12
>>> a=3
>>> b=3
>>> a|b
3
>>> a=5
>>> ~a
-6
>>> b=_4
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    b=_4
NameError: name '_4' is not defined. Did you mean: '_'?
>>> b=-4
>>> ~b
3
>>> -(b+1)
3
>>> -(a+1)
-6
>>> #xor ^
>>> a=4
>>> b=9
>>> a^b
13
>>> a=5
>>> b=10
>>> a^b
15
>>> 
>>> #<< (left shift)
>>> a=3
>>> a<<2
12
>>> a=5
>>> a<<3
40
>>> #>> (right shift)
>>> a=2
>>> a>>3
0
>>> a=4
>>> a>>7
0
