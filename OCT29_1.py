Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=["java","ai","ml"]
>>> len(a)
3
>>> b="java"
>>> len(b)
4
>>> c=["java"]
>>> len(c)
1
>>> a.count("ai")
1
>>> a.count(a)
0
>>> b=["java","ai","af"]
>>> b.count()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> b.count("a")
0
>>> b.count(ai)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b.count(ai)
NameError: name 'ai' is not defined. Did you mean: 'a'?
>>> 
>>> #tuple()
>>> a=(6,8.9,"python",2+9j,True,False)
>>> print(a)
(6, 8.9, 'python', (2+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.index(2)
ValueError: tuple.index(x): x not in tuple
>>> a.index(2+9j)
3
>>> a.count(True)
1
>>> len(a)
6
