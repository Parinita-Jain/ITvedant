'''
def fly(n):
    print(f"I am a {n}. I can fly.")
fly("bird")
fly("lion")
fly("fish")
'''
#--------------------
'''
class person:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
obj1=person()
obj1.walk()
obj1.talk()
print(type(obj1))
'''
#-----------------------
''''
class my_attributes:
    class_attr="This is a class attribute"
    def __init__(self):
        self.instance_attr="I am an object attribute"

obj1=my_attributes()
print(obj1.class_attr)
print(obj1.instance_attr)
obj1.class_attr="I am a class attr"
print(obj1.class_attr)
obj1.instance_attr="Hi"
print(obj1.instance_attr)

print("------------")

obj2=my_attributes()
print(obj2.class_attr)
print(obj2.instance_attr)
obj2.instance_attr="Object2"
print(obj2.instance_attr)

print(obj1.instance_attr)
print(obj2.instance_attr)

'''
#---------------
'''
class vehicle:
    def __init__(self,n,b,t):
        self.name=n
        self.brand=b
        self.type=t
    def display(self):
        print(f"{self.name} {self.brand} {self.type}")

car=vehicle("bmw n4","bmw x5","land")

ship=vehicle("cordelia","cruise","water")
#ship.inp()
car.display()
ship.display()
'''
#-------------
'''
class expl:
    def __init__(self):
        print("By default call")
    def hi(self):
        print("call me")

obj1=expl()
obj1.hi()
'''
#------------------
'''
a=20
b=30
print(f"Before swapping {a} {b}")
temp=a
a=b
b=temp
print(f"After swapping {a} {b}")

'''
#------------------------
'''
a=20
b=30
print(f"Before swapping {a} {b}")
b,a=a,b # tuple unpacking
print(f"After swapping {a} {b}")

'''
#-------------------
# 0, 1, 1,2,3,5,8,13,21
'''
a=0
b=1
n=9
x=[0,1]
for i in range(2,n):
    s=a+b
    x.append(s)
    a=b
    b=s
print(x)
'''
#----------------------
'''
class expl:
    def __init__(self): # constructor
        print("By default call")
    def hi(self):
        print("call me")
    def __del__(self): # destructor
        print("Object is deleted")

obj1=expl()
obj1.hi()
del obj1
#obj1.hi()
'''
#-----------------------
#Inheritance
# Single Inheritance
'''
class GrandParent:
    def land(self):
        print("Land")
class Parent(GrandParent):
    pass

obj1=Parent()
obj1.land()
'''
#--------------------
'''
#Multilevel Inheritance
class GrandParent:
    def land(self):
        print("Land")
class Parent(GrandParent):
    def ferrari(self):
        print("ferrari")

class U(Parent):
    def DubaiPlot(self):
        print("Dubai Plot")

obj1=Parent()
obj1.land()
obj1.ferrari()
happy=U()
happy.land()
happy.ferrari()
happy.DubaiPlot()
'''
#------------------------
'''
# Multiple Inheritance
class father:
    def land(self):
        print("Father's land")
        
class mother:
    def land(self):
        print("Mother's land")

class u(father,mother):
    def land(self):
        #super().land() # method overriding
        father.land(self)
        mother.land(self)
        print("Happy's land")
   

happy=u()
happy.land()
'''   
#-------------------
'''
from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def hi(self):
        print(hi)
class elephant(animal):
    def sound(self):
        print("Trumpet")
class horse(animal):
    def sound(self):
        print("Neigh")


e=elephant()
e.sound()
h=horse()
h.sound()
#a=animal() -- error
'''
#--------------------------
#------------- class/static attributes and static methods
'''
class calculator:
    pi=3.14 # class attribute / static attribute
    def __init__(self,r):
        # object attributes
        self.radius=r
    def display(self):
        print(calculator.pi*self.radius**2)
    @staticmethod
    def class_method():
        print(8*9)

circle=calculator(5)
print(circle.radius)
circle.display()
print(calculator.pi)
calculator.class_method()

'''
















































    















