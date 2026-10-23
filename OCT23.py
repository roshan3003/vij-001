Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a
a="vijayawada"
a[4]
'y'
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'

a[5]+a[6]
'in'
a[2]+a[3]
'am'
a[0]
'i'
a[2]
'a'
a="I am learning python full stack"
a[14]
'p'
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
'python'
'python'
a[5]
'l'
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
a[2]+a[3]
'am'
a[21]+a[22]+a[23]+a[24]
'full'
b="Time is very precious"
b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'precious'
b[8]+b[9]+b[10]+b[11]
'very'
b[0]+b[1]+b[2]+b[3]+b[4]
'Time '
a="Vijayawada is a royal city"
a[-1]
'y'
a[-8]
'y'
a[-4]
'c'
a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
a[-4]+a[-3]+a[-2]+a[-1]
'city'
a[-15]+a[-14]
'is'
b="vizag is a city of Destiny"
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'Destiny'
b[-15]+b[]+b[14]+b[13]+b[12]
SyntaxError: invalid syntax
b[-15]+b[-14]+b[-13]+b[-12]
'city'
b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'vizag'

#slicing
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'

a="work until you succeed"
a[:15]
'work until you '
a[15:]
'succeed'
a[5:]
'until you succeed'
a[5:10]
'until'
a[0:5]
'work '
a[0:4]
'work'
a[11:13]
'yo'
a[11:14]
'you'
b="simple is better than complex"
a[10:15]
' you '
b[10:!5]
SyntaxError: invalid syntax
b[10:15]
'bette'
b[10:16]
'better'
b[0:6]
'simple'
b[22:]
'complex'

a="Python is easy to learn"
a[-5:]
'learn'
>>> a[-13:-9]
'easy'
>>> 'easy'
'easy'
>>> a[-24:-18]
'Pytho'
>>> a[-24:-17]
'Python'
>>> b="God is great""
SyntaxError: unterminated string literal (detected at line 1)
>>> b="God is great"
>>> b[-5:]
'great'
>>> b[-7:-6]
's'
>>> b[-7:-5]
's '
>>> b[-8:-6]
'is'
>>> b[-12:-9]
'God'
>>> 
>>> #striding
>>> a="data science"
>>> a[::5]
'dsc'
>>> a[::2]
'dt cec'
>>> a[::1]
'data science'
>>> a="Cloud computing"
>>> a[::5]
'C u'
>>> a[::8]
'Cm'
>>> a[3:11]
'ud compu'
>>> a[5:]
' computing'
>>> a[:12]
'Cloud comput'
>>> a[::2]
'Codcmuig'
>>> a="Machine learing"
>>> a[1:9:2]
'ahn '
