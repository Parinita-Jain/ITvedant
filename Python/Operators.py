Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/FACULTY-CR2/Documents/ParinitaJain/9_11_2025/Python/area_calc.py
The area of Circle is : 153.86 and perimeter is : 43.96.
>>> a=True
>>> type(a)
<class 'bool'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a="True"
>>> type(a)
<class 'str'>
>>> a='a'
>>> a
'a'
>>> a=10
b=5
a+b
15
a-b
5
a*b
50
a/b
2.0
a/3
3.3333333333333335
a//3
3
a//b
2
a%b
0
a%3
1
a="Hello"
b="World"
a+b
'HelloWorld'
a-b
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
a*b
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
a*3
'HelloHelloHello'
a/b
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a/b
TypeError: unsupported operand type(s) for /: 'str' and 'str'
a=10
b=5
a**b
100000
r=7
r**2
49
2**3
8
3**2
9
3.14+20
23.14
a=3.14
b=20
c=a+b
c
23.14
type(c)
<class 'float'>
int(c)
23
d=int(c)
type(d)
<class 'int'>
e=str(c)
e
'23.14'
type(e)
<class 'str'>
