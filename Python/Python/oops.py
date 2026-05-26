'''
class GrandParent:
    def mansion(self):
        print(f"GP mansion of 100 crores")
class Parent(GrandParent):
    def __init__(self):
        self.land=int(input("Enter acres of land : "))
    def display(self):
        print(f"Parent has {self.land} acres of land")

class child(Parent):
    def __init__(self):
        self.area=int(input("Enter resort area : "))
    def display(self):
        print(f"{self.area} resort area")

c=child()
c.mansion()
c.display()
'''
#------------------------
'''
class M:
    def land(self):
        print("Mother's land")
class F:
    def land(self):
        print("Father's land")
class C(M,F): # compiler using Method Resolution Order(MRO)
    def land(self):
        #super().land()
        F.land(self)
        print("Child's land")
c=C()
c.land()

'''
#---------------------
'''
# Polymorphism
# +
# Method overriding - this is done during runtime
class animal:
    def sound(self):
        print("Some generic sounds")
class horse:
    def sound(self):
        print("Neigh")
class elephant:
    def sound(self):
        print("Trumpet")
class lamb:
    pass
for i in [animal(),horse(),elephant(),lamb()]:
    i.sound()
'''
#--------------------------
'''
from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        print("Generic Sound")
    def hear(self):
        pass
class horse(animal):
    def sound(self):
        animal.sound(self)
        print("Neigh")
class elephant(animal):
    def sound(self):
        print("Trumpet")
class lamb(animal):
    def sound(self):
        print("Blah")
for i in [horse(),elephant(),lamb()]:
    i.sound()

'''
#---------------------------------------
'''
class area:
    pi=3.14 # class variable
    def __init__(self):
        self.r=int(input("Enter radius : "))
        self.area=0
    def ar(self):
        self.area=area.pi*self.r*self.r
    def display(self):
        print(self.area)
        
a1=area()
a1.ar()
a1.display()

a2=area()
a2.ar()
a2.display()
'''
#-----------------------
# access modifiers

class person:
    def __init__(self):
        self.name=input("Enter name : ")
        self.__age=int(input("Enter age : "))

class person2(person):
    pass

f=person2()
print(f.name)
#print(f.__age)


















































