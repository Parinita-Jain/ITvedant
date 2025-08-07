'''
a=10
print(id(a))
b=10
print(id(b))
a=20
print(id(a))
print(id(b))
'''
#-----------------
'''
a=[] # empty list
print(a)
print(type(a))
print(id(a))
# append()
a.append(25)
print(a)
print(id(a))
#Apple, None,True , 10.5
'''
#-----------------------
'''
# put even numbers from 1 to 21 into a list
# if else
# loop , range(1,22)
a=[]
for i in range(1,21):
    if i%2==0:
        a.append(i)
print(a)
'''
#-------------
'''
# 67,89,50,43
even=list(range(0,101,2))
print(even)
odd=list(range(1,101,2))
print(odd)

'''
#----------------
'''
a=[]
a.append([67,89,50,43])
print(a)
a.extend([67,89,50,43]) # extend
print(a)

'''
#------------------
'''
l=["Apple","banana","Guava","Kiwi","Orange","Mango","Chikoo"]
m=[]# list()
# loop if true append elemenet in m
for i in l:
    if "a" not in i.lower():
        m.append(i)
print(m)
'''
#------------------
'''
l=["Apple","banana","Guava","Kiwi","Orange","Mango","Chikoo"]
l.remove("Guava")
print(l)
l.pop()
print(l)
#l.remove("Cherry") # error : Cherry not in list
print(l)

print(l[1]) # indexing
print(l) #['Apple', 'banana', 'Kiwi', 'Orange', 'Mango']
print(l[3])
print(l[2:4]) # slicing
'''
#--------------------------------
'''
l=["Apple","banana","Guava","Kiwi","Orange","Mango","Chikoo"]
print(len(l))
print(l[0:len(l):2])
print(l[::2])
print(l[::-1])
l.sort()
print(l)
l.reverse()
print(l)
'''
#---------------
'''
s="I take some word and make sentence"
for i in s:
    print(i,end="")
print()
s="Abhishek"
print(s[0]) #+ve indexing
print(s[-1]) # -ve indexing
print(s[len(s)-1]) # s[8-1]=s[7]=k # +ve indexing
print(s[-len(s)]) # s[-8] # -ve indexing

#
print(s[::-2]) #

'''
#----------------------------
'''
a="Apple"
a=12321
print(a,type(a))
a=str(a)
print(a,type(a))
if a[::]==a[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

'''
#----------------
'''
m=[]
for i in range(1,21):
    m.append(i**2)
print(m)

m=[i**2 for i in range(1,21)] # list comprehension
print(m)
'''
#--------------------------------
'''
m=[]
for i in range(1,21):
    if i%2==0:
        m.append(i**2)
print(m)

m=[i**2 for i in range(1,21) if i%2==0] # list comprehension
print(m)
'''
#----------------------
'''
l=list(range(1,21))
print(l)
'''
#----------------------
'''
l=[23,48,0,26,24,18,5,7,81]
m=[]
for i in l:
    if i%2==0:
        m.append("even")
    else:
        m.append("odd")
print(m)
print(l)


m=['even' if i%2==0 else "odd" for i in l ]
print(m)
print(l)
'''

#-------------------------
'''
l=[1,2]
print(l)
print(id(l))
l.append(True)
print(l)
print(id(l)) # list are mutable

m=[1,2]
n=[3,4]
print(m+n)
print(m*2)
'''
#-------------
'''
# tuple are immutable
t=()
print(t)
print(type(t))

t=tuple()
print(t)
print(type(t))     

t=tuple(range(0,21,2))
print(t)
print(type(t))

# (0, 2, 4, 6, 8,10, 12, 14, 16, 18, 20)

t=tuple(range(0,21,2))
print(t[5])
print(t[-6])
#+ve indexing
print(t[3:8:2])
print(t[-8:-3:2])
'''
#--------------------------
'''
# sets - mutable
s=set()
print(s)
print(type(s))
s={1,1,1,1,2,3,5,2,3,2,9,4,5}
print(s)
s={5,90,23,6,7,1,4}
print(s)
# there is no indexing and slicing in sets
#print(s[0])

s.add(100)
print(s)
s.discard(100)
print(s)
s.discard(100)
print(s)
s.remove(90)
print(s)
#s.remove(90)
print(s)
s.update([8,90,78])
print(s)

'''
#-------------------------
'''
s=set(range(1,4)) # 1,2,3
r=set(range(2,5)) # 2,3,4
print(s)
print(r)
print(s.union(r))
print(s.difference(r))
print(s.symmetric_difference(r))
print(s.intersection(r))
'''
#---------------------------
# dictionary- mutable , key-value pairs
'''
t=(1,)
print(t)
print(type(t))
s={1}
print(s)
print(type(s))

d={}
print(d)
print(type(d))


d=dict()
print(d)
print(type(d))

'''
#---------------------
'''
# keys should be immutable
student={"Name":["Alice","Joba","Atrice"],
         "Marks":(1,2,3,4,5),
         "Address":"Mumbai",
         1:20,
         20.9:56.45,
         (2,3,4,5):(7,8),
         (2,3,4,5):{7:67,8:90}}
print(student)

'''
#-------------------------
'''
student={"Name":"Alice",
         "Marks":100,
         "Course":"DSDA"}
print(student)

print(student["Name"]) # value as o/p

student["Name"]="Bob"
print(student)

student["Address"]="Andheri"
print(student)

print(student.get("Address")) # value as o/p - get()

print(student.keys())

print(student.values())

print(student.items())

print(student.pop("Course"))
print(student)

print(student.popitem())
print(student)

'''
#-----------------------
'''
# datetime
from datetime import datetime
# datetime -- module datetime class


print(datetime.now())
print(datetime.today())
a=datetime.now()
print(type(a))

s=a.strftime("%Y-%m-%d") # Converting datetime obj into string obj
print(s) # "2025-07-23"
print(type(s))

f=datetime.strptime(s,"%Y-%m-%d") # converting str obj into datetime obj
print(f)
print(type(f))

# date difference
from datetime import timedelta
delta = datetime(2025,7,19)-datetime(2025,7,23)
days=delta.days
print(days)

new_date=f+timedelta(days=-7)
print(new_date)

'''
#-------------------
'''
s="Hello"
print(s)
print(type(s))
print(id(s))
w="World"
s=s+w
print(s)
print(type(s))
print(id(s))

print(s)
s="Hello"+" "+"World ! How are you ?"
print(s[4]) #
print(s[6::-2])#

print(s[::-1])

print(s.lower())
print(s.upper())
print(s.strip())
print(s.replace("Hello","Great"))
print(s.split())
print(s.split("!"))
print(s.startswith("He"))
print(s.endswith("?"))
'''
#--------------------------
'''
s="Hello"+" "+"World ! How are you ?"
m=s.split()
counter=0
print(m)
for i in m:
    #print(f"{i} {len(i)}")
    if len(i)>3:
        counter=counter+1
print(f"{counter}")       

'''
#========================
emails=["abc@gmail.com","april@yahoo.com"]
d=[]
for i in emails:
    m=i.split("@")
    d.append(m[1])
print(d)


















































