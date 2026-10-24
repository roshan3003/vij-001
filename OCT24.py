Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="Machine learning"
a[1:9:2]
'ahn '
a[1:14:3]
'ai ai'
a[]2:13:4
SyntaxError: invalid syntax
a[2:13:4]
'cea'
a[6:15:5]
'er'
a[3:12:2]
'hn er'
a[4:14:6]
'ia'


a="python course"
a[-2:-10]
''
a[-2:-10:-3]
'son'
a[-3:-13:-4]
'r t'
a[-1:-12:-6]
'e '
a[-4:-9:-2]
'ucn'
a[::1]
'python course'
a[::-1]
'esruoc nohtyp'


#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1

#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("a")
1
a.count(" ")
3
a.count("x")
0
a=1,2,3,4
a.count(1)
1

#find a string
a="code"
a[2]
'd'
a.find("d")
2
b="hello"
b.find("1")
-1
b.find("l")
2
b[2:4]
'll'
>>> b.find("k")
-1
>>> ha
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    ha
NameError: name 'ha' is not defined. Did you mean: 'a'?
>>> 
>>> #escape sequences
>>> #\n->new line
>>> #\t-> tab space
>>> a="name  mobile number"
>>> print(a)
name  mobile number
>>> a="name\nmobileno\tmailid\ncollehe\tbranch"
>>> print(a)
name
mobileno	mailid
collehe	branch
>>> a="name:Roshan\nmobileno:5962686373\temail:roshan@gmail.com\ncollege:BITS\tbranch:bsc"
>>> print(a)
name:Roshan
mobileno:5962686373	email:roshan@gmail.com
college:BITS	branch:bsc
>>> 
>>> #replace()
>>> a="wait until you succeed"
>>> a.replace("wait,work")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.replace("wait,work")
TypeError: replace() takes at least 2 positional arguments (1 given)
>>> a.replace("wait","work")
'work until you succeed'
>>> a="python java"
>>> a.replace("java","DA")
'python DA'
>>> a="hi"
>>> a.replcae("hi","Me")
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.replcae("hi","Me")
AttributeError: 'str' object has no attribute 'replcae'. Did you mean: 'replace'?
>>> a.replace("hi","me")
'me'
