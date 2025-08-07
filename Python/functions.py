#-----------------
# 1st case
'''
def demo():
    a=input("Enter name : ")
    print(f"Hello {a} !")
    return None
print("Value returned by function ",demo())

'''
#--------------
'''
# 2nd case -- parameterized function
def demo(b):
    print(f"Hello {b} !")
    return None
a=input("Enter name : ")
print("Value returned by function ",demo(a))
'''
#--------------------
# 3rd case 
'''
def demo(b):
    print(f"Hello {b} !")
    #return "demo"
    return 3,4,5,6
a=input("Enter name : ")
u,v,w,x=demo(a) # (3,4,5,6) # tuple unpacking
print(f"{u} \n{v} \n{w} \n{x}")
'''
#----------------------
'''
def add(c,d):
    return c+d
def sub():
    a=int(input("Enter a number : "))
    b=int(input("Enter another number : "))
    print(a-b)

a=int(input("Enter a number : "))
b=int(input("Enter another number : "))
s=add(a,b)
print("Addition of numbers : ",s)
sub()

'''
#----------
'''
def inp():
    a=int(input("Enter a number : "))
    b=int(input("Enter another number : "))
    return a,b
def add():
    c,d=inp()
    return c+d
def sub():
    c,d=inp()
    return c-d
ad=add()
print(ad)
su=sub()
print(su)
'''
#-----------------------
# write fact with the help of functions 
'''
def fact(n): # n=5
    m=1
    for i in range(2,n+1): # 2,3,4,5 - range(2,6)
        m=m*i
    return m
c=fact(5)
print(c)
'''
#----------------------------
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
c=fact(5)
print(c)
'''
#--------------------------
'''
def fun(a,b):
    if b==0:
        return 1
    else:
        return a*fun(a,b-1)

c=3
d=4
print(fun(c,d))

'''
#-----------------
'''
def f(a,b,c=0,d=0): # default parameters
    print(a,b,c,d)
f(2,3,60,78,67,78,90,90)
'''

#-----------------------
'''
def f(*args): # variable length arguments
    print(args)
    print(type(args))
    s=0
    for i in args:
        s=s+i
    print(s)
f(2,3)

'''
#--------------
'''
import math
print(math.factorial(5))

'''
#-------------------
'''
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k} : {v} ")

f(a=1,b=4,c=2,d=6)

'''
#-----------------------
'''
def sq(n):
    return n**2
print(sq(6))
'''
#----------
'''
sq=lambda n:n**2
print(sq)
print(type(sq))
print(sq(6))

'''
#------------------------
'''
def f(a,b):
    return a+b
v=f(2,3)
print(v)
'''
#------------
'''
f=lambda a,b:a+b
v=f(2,3)
print(v)
'''
#------------
'''
def e_o(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
x=int(input("Enter a number : "))
v=e_o(x)
print(v)
'''
#-------------------------------
'''
e_o=lambda n:"even" if n%2==0 else "odd"

x=int(input("Enter a number : "))
v=e_o(x)
print(v)
'''
#-------------------------
'''
l=[12,2,6,8,7]
n=[]
for i in l:
    n.append(i**2)
print(n)
    
'''
#------------
'''
l=[12,2,6,8,7]
n=[i**2 for i in l]
print(n)
'''
#----------------
'''
def li_sq(x):
   return x**2
l=[12,2,6,8,7]
n=[]
for i in l:
    n.append(li_sq(i))    
print(n)
'''
#----------------
''''
l=[12,2,6,8,7]
n=list(map(lambda x:x**2,l))
print(n)
'''
#--------------------
'''
def e(x):
    if x%2==0:
        return True
    else:
        return False
l=[34,78,77,56,67,23,90]
n=[]
for i in l:
    n.append(e(i))    
print(n)
'''
#--------------------
'''
l=[34,78,77,56,67,23,90]
n=list(filter(lambda x:x%2==0,l))
print(n)
'''
#----------------------
'''
l=[4,5,2,3,7,6]
m=["A","B","C","D","E","F"]

print(list(zip(l,m)))
print(dict(zip(l,m)))

'''
#-----------------------
'''
import calculator as c
print(c.add(3,4))
print(c.sub(3,4))
'''
#----------
from calculator import add,sub
print(add(3,4))
print(sub(3,4))
#print(mul(3,4))









    













