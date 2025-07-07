'''
a=int(input("Enter number : "))
b=int(input("Enter number : "))
print("Addition : ",a+b)
print("Subtraction : ",a-b)
print("Multiplication : ",a*b)
print("Division : ",a/b)
'''
#--------------------------
'''
a=int(input("Enter number : "))
b=int(input("Enter number : "))
add=a+b
sub=a-b
mul=a*b
div=a/b
print("Addition : ",add)
print("Subtraction : ",sub)
print("Multiplication : ",mul)
print("Division : ",div)
'''
#----------------------
'''
def super_intelligent_friend():
    a=int(input("Enter number : "))
    b=int(input("Enter number : "))
    print("Addition : ",a+b)
    print("Subtraction : ",a-b)
    print("Multiplication : ",a*b)
    print("Division : ",a/b)

super_intelligent_friend()   

'''
#------------------------
'''
def inp():
    c=int(input("Enter number : "))
    d=int(input("Enter number : "))
    return c,d
    
def add_f():
    a,b=inp()
    print("Addition : ",a+b)
def sub_f():
    z,y=inp()
    print("Subtracion : ",z-y)
def mul_f():
    x,b=inp()
    print("Multiplication : ",x*b)
def div_f():
    u,v=inp()
    print("Division : ",u/v)
    
#add_f()
#sub_f()
#mul_f()
div_f()

'''
#------------------------
'''
def add_f():
    a,b=3,4
    return a+b
def sub_f():
    z,y=5,6
    return z-y
def mul_f():
    x,b=4,7
    return x*b
def div_f():
    u,v=4,9
    return u/v

add=add_f()
print("Addition : ",add)
sub=sub_f()
print("Subtracion : ",sub)
mul=mul_f()
print("Multiplication : ",mul)
div=div_f()
print("Division : ",div)
'''
#------------------------
'''
def add_f(a,b=1):
    return a+b
def sub_f(a,b=1):
    return a-b
def mul_f(x,b=4):
    return x*b
def div_f(u,x=2):
    return u/x

c=int(input("Enter number : "))
d=int(input("Enter number : "))
add=add_f(c,d)
#add=add_f(c)
print("Addition : ",add)
#sub=sub_f(c,d)
sub=sub_f(c)
print("Subtracion : ",sub)
mul=mul_f(c)
print("Multiplication : ",mul)
div=div_f(c)
print("Division : ",div)
'''
#-----------
'''
# factorial
a=1
n=5
for i in range(2,n+1):
    a*=i # a=a*i
print(a)

'''
#--------------------
'''
def fact(b,m):
    for i in range(2,m+1):
        b*=i # a=a*i
    return b

a=1
n=5
f=fact(a,n)
print(f)

'''
#------------
'''
import math
print(math.factorial(6))
'''
#-----------------
'''
def display(m):
    for i in m:
        print(i)
l=list(range(1,12,2))
print(display(l))
'''
#------
'''
def display(*args): # variable length argument *args
    print(sum(args))

display(1,2,3,4,5,6,7,8,9,10)

'''
#-----------
'''
def display(**kwargs): # key word args
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k} : {v}")
display(A=1,B=4)
'''
#--------------------
'''
# variable
name="Modi"# global variable

def f():
    #global name
    name="Tapan" # local variable
    print(name)
 
print(name)
f()
print(name)

'''
#--------------------
'''
def sq(n):
    return n**2
m=6
c=sq(m)
print(c)
'''
#----------------------
'''
sq= lambda n:n**2
print(sq(6))
print(type(sq))
'''
#--------------------
'''
def add(a,b):
    return a+b
c=2
d=3
print(add(c,d))
'''
#---------------
'''
add = lambda a,b:a+b
c=2
d=3
print(add(c,d))
'''
#--------------------
'''
def e(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

print(e(21))

'''
#---------------
'''
e=lambda n:"even" if n%2==0 else "Odd"
print(e(21))

'''
#-----------------
'''
def s(v):
    return v.split()
t="""A sentence is a group of words that expresses a complete thought
and typically contains a subject and a verb"""

print(s(t))
'''
#-----------
'''
s=lambda v:v.split()
t="""A sentence is a group of words that expresses a complete thought
and typically contains a subject and a verb"""

print(s(t))
'''
#---------------------
'''
l=[1,23,67,89,92,44]
m=[]
for i in l:
    if i%2==0:
        m.append(i)
print(m)
'''  
#-----------------------
'''
l=[1,23,67,89,92,44]

m=[i for i in l if i%2==0]
print(m)
'''      
#------------------
'''
a=[1,23,67,89,92,44]
def e(b):
    n=[i for i in b if i%2==0]
    return n
n=e(a)
print(n)
'''
#--------------
'''
a=[1,23,67,89,92,44]
n=list(filter(lambda x:x%2==0,a))
print(n)
'''
#---------------------
'''
a=[1,23,67,89,92,44]
def e(b):
    print(b)
    if b%2==0:
      return b
print(a)
n=list(filter(e,a))
print(n)
'''
#-----------------------
'''
l=[4,8,3,2,7,6]
n=[]
for i in l:
    n.append(i**2)
print(n)
'''
#---------------
'''
l=[4,8,3,2,7,6]
def f(a):
    print("Parameter a value inside function : ",a)
    n=[]
    for i in a:
        print("i : ",i)
        n.append(i**2)
        print("n : ",n)
    return n 
print(f(l))
    
'''
#--------------------
'''
l=[4,8,3,2,7,6]
n=list(map(lambda x:x**2,l))
print(n)
'''
#-----------------
'''
a1=[1,2,3]
b1=[4,5,6]
print(list(zip(a1,b1)))
print(dict(zip(a1,b1)))
'''
#-------------------
'''
l=[1,2,3,4,5]
a=0
for i in l:
    print(f"Before manipulation : a : {a}  i:{i}")
    a+=i # a=a+i
    print(f"After manipulation : a : {a}  i:{i}")
print(a)
'''
#--------------
'''
from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda x,y:x*y,l))

'''
#------------------
'''
import calculator
print(calculator.add(2,3))

'''
#-----------
'''
import calculator as c
print(c.add(2,3))
print(c.mul(2,3))
'''
#------------
'''
from calculator import add,mul
print(add(2,3))
print(mul(2,3))
'''
#------------
def f(n):
    if n==1:
        return n
    else:
        return n*f(n-1)
print(f(5))










































    











