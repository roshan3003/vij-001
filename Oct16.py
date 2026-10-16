Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int()
int(9)
9
int(9.2)
9
int('hi')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int('hi')
ValueError: invalid literal for int() with base 10: 'hi'
int(7+9j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(7+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
float(9)
9.0
float(9.3)
9.3
float('hi')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float('hi')
ValueError: could not convert string to float: 'hi'
float(7+3h)
SyntaxError: invalid decimal literal
float(True)
1.0
>>> float(False)
0.0
>>> str(9)
'9'
>>> str(8.3)
'8.3'
>>> str('hi')
'hi'
>>> str(4+2k)
SyntaxError: invalid decimal literal
>>> str(4+2j)
'(4+2j)'
>>> float(3+3j)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    float(3+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> str(True)
'True'
>>> str(False)
'False'
>>> complex(9)
(9+0j)
>>> complex(9+1j)
(9+1j)
>>> complex('hi')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    complex('hi')
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> bool(9)
True
>>> bool(9.2)
True
>>> bool('hi')
True
>>> bool(9+7j)
True
>>> bool(True)
True
>>> bool(False)
False
