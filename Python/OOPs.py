'''
m=1
for i in range(1,8):
    m=m*i
print(m)
l=list(range(1,8))
print(l)
m=0
for i in range(1,8):
    m=m+i
print(m)
'''
#------------------

# Object Oriented Programming System (OOPs)
'''
def fly(n):
    print(f"{n} can fly")
fly("Birds")
fly("Bat")
fly("Horse")
'''
#-------------------
'''
class vehicle:
    def assign(self,name,mode): # assign -- method of the object
        self.n=name # n and m -- attributes of a object
        self.m=mode
    def display(self):
        print(f"I am a {self.n}. My mode of transport is {self.m}")
    def hello(self):
        print("Hi !!")
        
v=vehicle() # v is the object of type vehicle
v.assign("Car","Land")
v.display()
v.hello()

a=vehicle()
a.assign("Aeroplane","Air")
a.display()
a.hello()

'''
#---------------
'''
class vehicle:
    def __init__(self,name,mode): # constructor
        self.n=name # n and m -- attributes of a object
        self.m=mode
    def display(self):
        print(f"I am a {self.n}. My mode of transport is {self.m}")
    def hello(self):
        print("Hi !!")
    def __del__(self): # destructor
        print("Object Deleted")
        
v=vehicle("Car","Land") # v is the object of type vehicle
v.display()
v.hello()

a=vehicle("Aeroplane","Air")
#a.assign("Aeroplane","Air")
a.display()
a.hello()
print(type(a))

del v
'''
#----------
'''
class A:
    def display(self):
        print("Hello")
class B(A):
    def hello(self):
        print("B hello")
class C(B):
    pass

b=B()
b.display()
c=C()
c.display()
c.hello()
'''
#----------
'''
m=[]
l=["April","Bob","Tom","Jerry"]
for i in l:
    if "o" not in i:
        m.append(i)
        
print(m)
m=[i for i in l if "o" not in i] # list comprehension
print(m)

'''
#--------------------
'''
def y1(x):
    if x%2!=0:
        print("odd")
    else:
        print("even")

y=lambda x:"odd" if x%2!=0 else "even"
print(y(50))
y1(5)

'''
#------------
'''
# fibonacci series
for i in range(0,9):
    if i==0:
        print(0,end=" , ")
        a=0
    elif i==1:
        print(1,end=" , ")
        b=1
    else:
        """
        a,b=b,a+b
        print(b,end=" , ")
        """
        c=a
        a=b
        b=a+c
        print(b,end=" , ")

'''
#-------------
# hierarchical inheritance
# 1 parent class Many child class
'''
class Parent:
    def display(self):
        print("Parent class A")
class B(Parent):
    pass

class C(Parent):
    pass

b=B()
b.display()
c=C()
c.display()
'''
#------------------------
# Multiple Inheritance
# Many Parents 1 Child--
'''
class Father:
    def display(self):
        print("Father Display Method")
class Mother:
    def display(self):
        print("Mother display method")
class child(Father,Mother):
    def display(self):
        super().display()
        Father.display(self) #-------------
        Mother.display(self)
        print("Child display method")

c=child()
c.display()
# super()
f=Father()
f.display()
'''
#--------------------------
#Polymorphism -- Over riding (Over loading not directly supported)
# abstract classes
# Abstract base class
# abc module
# @abstractmethod -- @ is a decorator
# Method overriding
'''
from abc import ABC,abstractmethod
class animal:
    @abstractmethod
    def sound(self):
        pass
class horse(animal):
    def sound(self):
        print("Neigh")

h=horse()
h.sound()
class elephant(animal):
    def sound(self):
        print("trumpet")
    

e=elephant()
e.sound()
'''
#----------
'''
# method overloading
class add:
    def add(self,a,b,c=0,d=0):
        print(a+b)
    def additi(self,*args):
        print(sum(args))

a=add()
a.add(2,3,4)
a.additi(8,7,8,7,8,7,8,9,0)
'''
#-----------------------
'''
class product:
    c=1
    def __init__(self):
        #self.id=i
        self.id=product.c
        product.c+=1
    def get_product_details(self,n,p,q):
        self.name=n
        self.price=p
        self.quantity=q
    def display_product(self):
        print(f"{self.id} , {self.name} , {self.price} , {self.quantity}")
count=1     
pr=product()
count=count+1
pr.get_product_details("Mobile",12000,4)
pr.display_product()

pr=product()
count=count+1
pr.get_product_details("Mobile",12000,4)
pr.display_product()

'''
#---------------------------
class product:
    # class atribute
    c=1
    def __init__(self):
        self.id=product.c
        product.c=product.c+1
        self.name=""
        self.price=0
        self.quantity=0
    def get_product_details(self):
        self.name=input("Enter Name of Product : ")
        self.price=int(input("Enter Price of Product : "))
        self.quantity=int(input("Enter Quantity of Product : "))
    def display(self):
        print(f"{self.id} {self.name} {self.price} {self.quantity}")

p1=product()
p1.get_product_details()
p1.display()

p2=product()
p2.get_product_details()
p2.display()

p3=product()
p3.get_product_details()
p3.display()











