Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,"python",8+9j,True,False]
print(a)
[2, 4.5, 'python', (8+9j), True, False]
type(a)
<class 'list'>
b=4.6
type(b)
<class 'float'>
c=[4.6]
type(c)
<class 'list'>

a=["python","java","c","c++"]
a.append("ai")
a
['python', 'java', 'c', 'c++', 'ai']
a.append("ml","dsa")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ml","dsa")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","dsa"])
a


a
['python', 'java', 'c', 'c++', 'ai', ['ml', 'dsa']]

#extend()
a=["dsa","ai","ml"]
a.extend(["python","java"])
a
['dsa', 'ai', 'ml', 'python', 'java']

#insert()
b=["black","white"]
b.insert(1,"red")
b
['black', 'red', 'white']

#index
a=["apple","mango","kiwi","grape"]
a.index("kiwi")
2
a.copy()
['apple', 'mango', 'kiwi', 'grape']
b=a.copy()
b
['apple', 'mango', 'kiwi', 'grape']

#pop
a=["vij","blr","vzg"]
a.pop()
'vzg'
a
['vij', 'blr']
a.pop(1)
'blr'

a
['vij']
a.pop(0)
'vij'
a
[]

#remove()
a=["hi","hello","how"]
a
a.remove("how")
a
['hi', 'hello']

a
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list

a=["java","ai","ml"]
a.clear()
a
[]
b=[]
b.append("roshan")
>>> b
['roshan']
>>> 
>>> a=["banana","grapes","apple","mango","kiwi"]
>>> a.sort()
>>> a
['apple', 'banana', 'grapes', 'kiwi', 'mango']
>>> b=[1,4,2,5,7,4,5]
>>> b.sort()
>>> b
[1, 2, 4, 4, 5, 5, 7]
>>> c=[5+9j,2+4j,6+9j]
>>> c.sort()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'complex' and 'complex'
>>> c=[3.2,8.6,9.,2.5,6.1]
>>> c.sort()
>>> c
[2.5, 3.2, 6.1, 8.6, 9.0]
>>> d=[True,False,True]
>>> d.sort(0d.sort()
...        
SyntaxError: invalid decimal literal
>>> 
>>> d.sort()
...        
>>> d
...        
[False, True, True]
>>> 
>>> a=["red","green","blue"]
...        
>>> a.reverse()
...        
>>> a
...        
['blue', 'green', 'red']
>>> b=[5,8,55,5,9]
...        
>>> b.reverse()
...        
>>> b
...        
[9, 5, 55, 8, 5]
