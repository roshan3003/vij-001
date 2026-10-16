Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=10
>>> type(a)
<class 'int'>
>>> b=5.4
>>> print(b)
5.4
>>> c='python'
>>> print(c)
python
>>> c='python'
>>> type(c)
<class 'str'>
>>> b=4.2
>>> type(b)
<class 'float'>
>>> d="code"
>>> tyoe(d)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    tyoe(d)
NameError: name 'tyoe' is not defined. Did you mean: 'type'?
>>> d="code"
>>> type(d)
<class 'str'>
>>> e='''code'''
>>> type(e)
<class 'str'>
>>> f=4+9j
>>> type(f)
<class 'complex'>
>>> g=21+4j
>>> type(f)
<class 'complex'>
>>> x=2j
>>> type(x)
<class 'complex'>
>>> y=3f+1
SyntaxError: invalid decimal literal
>>> c=True
>>> type(c)
<class 'bool'>
>>> b=  False
>>> type(b)
<class 'bool'>
