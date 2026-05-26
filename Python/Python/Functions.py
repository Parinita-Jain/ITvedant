'''
def a():
    print("Good morning !")
    #return 354728," Hey! Hope u r good", "ityu"
    return None

for i in range(0,10):
    print(a())
'''
#--------------------
#"I like python"
'''
def pl():
    print("I like python")
pl()
'''
#---------------------
'''
def r():
    return "I like python"
a=r()
print(a.upper())
print("I like python")
print(r().upper())

'''
#----------------
'''
a=input("Enter name : ")
print(a)

def g():
    a=input("Enter name : ")
    print(a)
g()
    
'''
#-------------------------------------------
'''
def g(b):
    print(b)

a=input("Enter name : ")
g(a)
'''
#--------------------
'''
def g():
    a=input("Enter name : ")
    return int("7")
b=g()
print(b)  
'''
#---------------------
'''
a=int(input("Enter number : ")) #7
print(type(a))
m=1
for i in range(1,a+1):
    m=m*i
print(m)
'''
#-------------------
'''
def f(r):
    m=1
    for i in range(1,r+1):
        m=m*i
    return m
    
a=int(input("Enter number : "))
c=f(a)
print(c)

'''
#-----------
'''
def f():
    a=int(input("Enter number : "))
    m=1
    for i in range(1,a+1):
        m=m*i
    return m
c=f()
print(c)
'''
#---------------
'''
def f(a,b,c,d):
    print(a,b,c,d)
    print(a+b+c+d)
m,n,o,p=1,2,3,4
f(m,n,o,p)
'''
#-----------------
'''
def f(a,b,c=0,d=0):
    print(a,b,c,d)
    print(a+b+c+d)
m,n=1,2
f(m,n,3)
'''
#--------
'''
#*args : variable length arguments
def f(*args):
    print(*args)
    print(args)
    print(type(args))
    print(sum(args))
m,n=1,2
f(m,n,3,4,5,6,7,8,9)
'''
#------------
'''
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs.items())
    for k,v in kwargs.items():
        print(k,v)

f(m=1,n=2,o=3,p=4)

'''
#----------
# func with arg also called as parameterized function
# which will return square of a number
'''
a=int(input("Enter number : "))
c=a*a
d=a**2
print(c,d)
'''
#---------
'''
def f(r):
    return r*r
a=int(input("Enter number : "))
c=f(a)
print(c)
'''
#------------------------------------------------------
'''
f=lambda r:r*r

a=int(input("Enter number : "))
c=(f(a))
print(c)

'''
#------------------
'''
#a=1,b=2,c=3,d=4
def g(u,v,w,x):
    return u+v+w+x
print(g(1,2,3,4))

g=lambda u,v,w,x:u+v+w+x
print(g(1,2,3,4))

'''
#-----------------
'''
l=[12,3,6,8,9,10]
n=[]
for i in l:
    n.append(i**2)
print(n)
'''
#----------------
'''
def sq(x):
    return x**2
l=[12,3,6,8,9,10]
n=[]
for i in l:
    n.append(sq(i))
print(n)

'''
#-------------------
'''
n=list(map(lambda x:x**2,[12,3,6,8,9,10]))
print(n)

l=["Apple","Banana","cherry","dRagon fruit"]
n=list(map(lambda x:x.upper(),l))
print(n)

'''
#------------
'''
def e_o(x):
    if x%2==0:
        return True
    else:
        return False
l=[12,3,6,8,9,10]
n=[]
for i in l:
    a=e_o(i)
    if a==True:
        n.append(i)
print(n)


l=[12,3,6,8,9,10]
n=list(filter(lambda x:x%2==0,[12,3,6,8,9,10]))
print(n)

o=list(filter(lambda x:x%2!=0,[12,3,6,8,9,10]))
print(o)
'''
#------------------------
'''
L1=[1,2,3,4]
L2=[1,4,9,16]
d={}

for i in range(1,len(L1)+1):
    d[i]=L2[i-1]
print(d)


f=zip(L1,L2)
print(dict(f))
'''
#---------------------
'''
L2=[1,2,3,4,5]
from functools import reduce
s=reduce(lambda x,y:x+y,L2)
print(s)

'''
#-----------------
'''
import calculator
print(calculator.add(30,40))
print(calculator.mul(30,40))
'''
#-----------------
'''
import calculator as c
print(c.add(30,40))
print(c.mul(30,40))

'''
#-------------------
'''
from calculator import sub,div
print(sub(40,3))
print(div(40,3))
#print(mul(40,3))
'''
#----------
'''
def f3():
    print("Divisible by 3")
def f2():
    print("Remainder 2")
def f1():
    print("Remainder 1")
def f0():
    i=int(input("Enter number : "))
    if i%3==0:
        f3()
    elif i%3==1:
        f1()
    else:
        f2()
f0()
'''
#-------------------
'''
def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)

print(fact(5))

'''
#---------------
'''
n=int(input("Enter number : "))
if n==0 or n==1:
    print("1")
else:
    m=1
    for i in range(1,n+1):
        m=m*i
    print(m)
'''
#-----------
'''
def fly(n):
    print(f"Hi ! Im a {n}. I can fly")
fly("Butterfly")
fly("Elephant")
fly("Class A334")

print(3+4)
print("A"+"B")
'''
#--------
'''
class A:
    def greetings(self):
        print("Hello from class A")

obj1=A()
print(type(obj1))
obj1.greetings()

class Bird:
    def fly(n):
     print(f"Hi ! Im a {n}. I can fly")

b=Bird()
b.fly()

# Object oriented programming
'''
#-----------------------

# student - name marks attribute/properties of student
'''
class student:
    def inp(self,n,m):
        self.name=n
        self.marks=m
    def disp(self):
        print(f"{self.name} , {self.marks}")
obj1=student()
obj1.inp("Sohan",98)
obj1.disp()

obj2=student()
obj2.inp("Vatsal",99)
obj2.disp()

obj3=student()
obj3.inp("Vijay",98)
obj3.disp()

obj4=student()
obj4.disp()
'''
#---------------------
'''
class student:
    def __init__(self,n,m): # constructor
        self.name=n
        self.marks=m
    def disp(self):
        print(f"{self.name} , {self.marks}")
    def __del__(self):
        print("Hi ! Im deleted")


obj1=student("Sohan",98)
obj1.disp()
del obj1
'''
#----------------
class student:
    def __init__(self,n,r,m):
        self.name=n
        self.roll=r
        self.marks=m
    def display_details(self):
        print(f"{self.name}\n{self.roll}\n{self.marks}")
    def grade(self):
        if 75<=self.marks<=100:
            return "A"
        elif 60<=self.marks<=74:
            return "B"
        elif 35<=self.marks<=59:
            return "C"
        else:
            return "F"

s1=student("April",1,89)
s1.display_details()
print(s1.grade())






