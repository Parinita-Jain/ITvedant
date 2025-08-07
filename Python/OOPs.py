'''
def fly(n):
    print(f"Hi ! I'm a {n}. I can fly")
fly("bird")
fly("crocodile")
fly("donkey")
'''
#------------
'''
a=1
b=2
print(type(a))
print(type(b))
print(a/b)


a='1'
b='2'
print(type(a))
print(type(b))
print(a/b)
'''
#-------------------------------
'''
class bird:
    def prop(self,w,t):
        self.wings=w
        self.tail=t
    def display(self):
        print(f"""Hi ! Im a bird. I have {self.wings} wings ,
                  tail {self.tail} cm""")
    def fly(self):
        print("I fly with my {self.wings} wings")

crow=bird()
#crow.prop("black",2)
crow.display()
crow.fly()
print(crow.wings)
print(crow.tail)
'''
#--------------------
'''
class bird:
    def __init__(self,w,t):
        self.wings=w
        self.tail=t
    def display(self):
        print(f"""Hi ! Im a bird. I have {self.wings} wings ,
                  tail {self.tail} cm""")
    def fly(self):
        print("I fly with my {self.wings} wings")

crow=bird("black",2)
#crow.prop("black",2)
crow.display()
crow.fly()
print(crow.wings)
print(crow.tail)


'''
#----------------------
'''
class student:
    def __init__(self,i,n,m):
        self.id=i
        self.name=n
        self.marks=m
    def display(self):
        print(f"{self.id} {self.name} {self.marks}")
    
a=student(1,"April",56)
a.display()

b=student(2,"Autumn",68)
b.display()

class employee:
    def __init__(self,i,n,s):
        self.id=i
        self.name=n
        self.salary=s
    def display(self):
        print(f"{self.id} {self.name} {self.salary}")
    def __del__(self):
        print("Hi ! I'm deleted")


a=employee(1,"April",56000)
a.display()

b=employee(2,"Autumn",68000)
b.display()
del b
b.display()

#OOP __init__() __del__()
# encapsulation inheritance
'''
#---------------------
# single inheritance
'''

class gp:
    def land(self):
        print("I have 1000 acres of land. I will give to my children.")

class f(gp): # inheritance
    pass
    
obj=f()
obj.land()
'''
#---------------
# Multilevel inheritance
'''
class gp:
    def land(self):
        print("I have 1000 acres of land. I will give to my children.")

class f(gp): # inheritance
    def dubai_flat(self):
        print("I have flat in dubai. I will give to my children.")
        
class u(f):
    pass
obj=u()
obj.land()
obj.dubai_flat()
'''
#-------------------------------
# multiple inheritance
'''
class father:
    def land(self):
        print("Father's land")
class mother:
    def land(self):
        print("Mother's land")
class u(father,mother):
    def land(self):
        #super().land()#Method resolution order(MRO),
        #this will call father first
        father.land(self) # explicit method call
        mother.land(self)
        print("Proudly my land")
obj=u()
obj.land()
    
'''
#-------------------------------
# polymorphism
'''
class animals:
    def make_sound(self):
        print("Generic Sound")

class cat(animals):
    def make_sound(self):
        print("Meow")
    
class horse(animals):
    def make_sound(self):
        print("Neigh")

l=[animals(),cat(),horse()] # method overriding happening at runtime
for i in l:
    i.make_sound()
'''
#---------------
'''
# Abstraction - Abstract Base Class (ABCs) , abc module
# @abstractmethod decorator

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        #print("Animals make sound.")
        pass
class horse(Animal):
    def sound(self):
        #Animal.sound(self)
        return "Neigh"
class cat(Animal):
    def sound(self):
        return "Meow"
class elephant(Animal):
    def sound(self):
        return "Trumpet"

l=[cat(),horse(),elephant()] 
for i in l:
    print(i.sound())

'''
#--------------------------
'''
class area:
    pi=3.14 # class attribute/ststic attribute shared among all objects of class
    def __init__(self,r):
        self.radius=r
    def ar_cal(self):
        ar=area.pi*self.radius
        return ar
    def display(self,ar):
        print(f"The area is : ",ar)

a=area(2)
ar=a.ar_cal()
a.display(ar)
'''
#--------------------------
'''
# access modifiers in python 
class person:
    def __init__(self,n):
        self.__name=n # private attribute
    def display_name(self):
        print(f"Hello {self.__name}")
p=person("April")
p.display_name()
# p.__name

'''
#-----------------------------


























