Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
a
10
b
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    b
NameError: name 'b' is not defined

========================= RESTART: E:/ParinitaJain/Python/demo.py =========================
10

========================= RESTART: E:/ParinitaJain/Python/demo.py =========================
10
20
20
20+30
50
20+60
80
30+60
90
(30+60)*0.01
0.9
A=20
A
20
a
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?
a=10
a
10
A
20
# Case Sensitive



a=20
a
20
A=10
A
10
a
20
A
10
type(a)
<class 'int'>
a="ABC"
type(a)
<class 'str'>
a=10.67
type(a)
<class 'float'>
a=True
type(a)
<class 'bool'>
a
True
a=true
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a="true"
type(a)
<class 'str'>
a="1"
type(a)
<class 'str'>
a*3
'111'
a*10
'1111111111'
type(a)
<class 'str'>
a/10
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a/10
TypeError: unsupported operand type(s) for /: 'str' and 'int'
a=1
a/10
0.1
a=1
b=2
a+b
3
a="1"
b="2"
a+b
'12'
a
'1'
a1=200
1a=200
SyntaxError: invalid decimal literal
a15421436568780689=90
15421436568780689a=40
SyntaxError: invalid decimal literal
_a=10
a_=20
a@=10
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a@=10
TypeError: unsupported operand type(s) for @=: 'str' and 'int'
a.=10
SyntaxError: invalid syntax
a#10
'1'
a*10
'1111111111'
a#526578
'1'
a=b=c=10
a
10
b
10
c
10
a,b,c=1,3,5
a
1
b
3
c
5
a=[7+5-9*8]
a
[-60]
a=[7+\
   5\
   -9\
   *8]
a
[-60]
#fgfghfghh
fghfghgjh
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    fghfghgjh
NameError: name 'fghfghgjh' is not defined
a=fghfghgjh
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a=fghfghgjh
NameError: name 'fghfghgjh' is not defined
"fghfghgjh"
'fghfghgjh'
1
1
'fghfghgjh'
'fghfghgjh'
'fghfghgjh"
SyntaxError: unterminated string literal (detected at line 1)
#yuiyti,jhhmh hihg hjn rt
'''
this
is
an example
of
multiline
comment
'''
'\nthis\nis\nan example\nof\nmultiline\ncomment\n'
"""this\nis\nexample"""
'this\nis\nexample'
a
[-60]
b
3
a\nb
SyntaxError: unexpected character after line continuation character
print(a)
[-60]
print(a,"\n",b)
[-60] 
 3
>>> print("a\nb")
a
b
>>> a=10
>>> b=5
>>> a+b
15
>>> a-b
5
>>> a*b
50
>>> a/b
2.0
>>> a^b
15
>>> a**b
100000
>>> 15
15
>>> a**b
100000
>>> a//b
2
