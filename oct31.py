Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[9,1,5,2,8,4,6,3,7,0]
... # [7,6,4,3,0,9,8,5,2,1]
>>> left=a[0:5]
>>> left
[9, 1, 5, 2, 8]
>>> right=a[5:10]
>>> right
[4, 6, 3, 7, 0]
>>> left.sort()
>>> left
[1, 2, 5, 8, 9]
>>> right.sort()
>>> right
[0, 3, 4, 6, 7]
>>> left.reverse()
>>> left
[9, 8, 5, 2, 1]
>>> right.reverse()
>>> right
[7, 6, 4, 3, 0]
>>> c=right+left
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> 
>>> #dictionary{}
>>> a={"name":"pooja","year":2026,"month":10}
>>> print(a)
{'name': 'pooja', 'year': 2026, 'month': 10}
>>> type(a)
<class 'dict'>
>>> b={"name","pooja","year",2026}
>>> print(b)
{'pooja', 'name', 'year', 2026}
>>> type(b)
<class 'set'>
>>> <class 'set'>
SyntaxError: invalid syntax
>>> 
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['pooja', 2026, 10])
a.items()
dict_items([('name', 'pooja'), ('year', 2026), ('month', 10)])
b={1:2,3:4}
type(b)
<class 'dict'>
b.keys()
dict_keys([1, 3])

a={"course":"python","code":"gnan","data":"coding"}
a["course"]
'python'
a
{'course': 'python', 'code': 'gnan', 'data': 'coding'}
a["python"]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a["python"]
KeyError: 'python'
a.get("code")
'gnan'
a
{'course': 'python', 'code': 'gnan', 'data': 'coding'}

#update
a={"year":2026,"month":11}
a.update({"time":10})
a
{'year': 2026, 'month': 11, 'time': 10}
a.update({"hour":1},{"min":10})
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.update({"hour":1},{"min":10})
TypeError: update expected at most 1 argument, got 2
a.update({"hour":1,"min":10})
a

a
{'year': 2026, 'month': 11, 'time': 10, 'hour': 1, 'min': 10}

#setdefault
a={"colour":"black","food":"biryani","desert":"cake"}
a.setdefault("place","vij")
'vij'
a
{'colour': 'black', 'food': 'biryani', 'desert': 'cake', 'place': 'vij'}

a.pop("colour")
'black'
a
{'food': 'biryani', 'desert': 'cake', 'place': 'vij'}
a.popitem()
('place', 'vij')
a
{'food': 'biryani', 'desert': 'cake'}

#copy
a={"hour":10,"min":11,"sec":5}
a.copy()
{'hour': 10, 'min': 11, 'sec': 5}
b=a.copy()
b
{'hour': 10, 'min': 11, 'sec': 5}
a.clear()
a
{}
b
{'hour': 10, 'min': 11, 'sec': 5}
a.copy()
{}

a={"name"}
;
a={"name":"roshan","city":"vja","name":"roshan"}
print(a)
{'name': 'roshan', 'city': 'vja'}
a={"name":"roshan","city":"vja","name":"sonu"}
pirnt(a)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    pirnt(a)
NameError: name 'pirnt' is not defined. Did you mean: 'print'?
print(a)
{'name': 'sonu', 'city': 'vja'}
a={"name":"roshan","city":"vja","name2":"sonu"}
print(a)
{'name': 'roshan', 'city': 'vja', 'name2': 'sonu'}

a={"idnos":[10,20,30],"names":["roshan","sonu","code"],"marks":[60,70,80]}
print(a)\
print(a)
SyntaxError: invalid syntax
print(a)
{'idnos': [10, 20, 30], 'names': ['roshan', 'sonu', 'code'], 'marks': [60, 70, 80]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names', 'marks'])
a.values()
dict_values([[10, 20, 30], ['roshan', 'sonu', 'code'], [60, 70, 80]])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['roshan', 'sonu', 'code']), ('marks', [60, 70, 80])])
