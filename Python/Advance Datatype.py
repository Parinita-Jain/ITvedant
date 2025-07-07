'''
l=list()
print(l)
print(type(l))

l=[]
print(l)
print(type(l))

l=["Apple","Banana","Cherry","Dragon Fruit"]
print(l)
print(type(l))
'''
#--------------------
'''
a=["Apple","Banana","Cherry",None,True,1,10.0,1+2j]

print(a)
print(type(a))

print(a[0])
print(a[5])
print(a[-1])
print(len(a))
print(a[len(a)-1])
print(a[-len(a)])
print(a[::2])
print(a[1::2])
print(a[::-1])

a=["Apple","Banana","Cherry",None,True,1,10.0,1+2j]
for i in a:
    print(i)

for i in "Yesterday":
    print(i)


a=list(range(20))
print(a)
'''
#---------------
'''
a=[]
print(a)
a.append(1)
print(a)
a.append([2,3,4])
print(a)
a.extend([78,89,90])
print(a)
a.insert(2,40)
print(a)
a.remove(1)
print(a)
a.extend([1,1,1,1,1])
a.remove(1)
print(a)
a.pop()
print(a)
a.count(1)
print(a)
print(a[0][1])
a.remove([2,3,4])
a.sort()
print(a)
a.sort(reverse=True)
print(a)
del a
'''
#----------------
'''
l=[]
for i in range(2,41,2):
    l.append(i)
print(l)

#--------
l=[]
for i in range(1,41):
    if i%2==0:
        l.append(i)
print(l)
'''
#-----------------------
'''
l=list(range(2,41,2))
print(l)
'''
#---------------------
'''
l=[]
for i in range(1,11):
    if i%2==0:
        l.append("even")
    else:
        l.append("odd")
print(l)
    
'''
#-------------------------
'''
l=[12,71,23,18,6,2,5,7,541]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append("even")
    else:
        odd.append("odd")
print(even)
print(odd)
if len(even)==len(odd):
    print("Same lengh")
elif len(even)>len(odd):
    print("More even numbers")
else:
    print("More odd numbers")
        
'''
#------------------
'''
l=[]
for i in range(2,41,2):
    l.append(i)
print(l)
'''
#--------------
# list comprehension
'''
l=[i for i in range(2,41,2)]
print(l)
'''
#-------------
'''
l=[]
for i in range(1,41):
    if i%2==0:
        l.append(i)
print(l)
'''
#------------------
'''
l=[i for i in range(1,41) if i%2==0]
print(l)
'''
#---------------
'''
l=[]
for i in range(1,11):
    if i%2==0:
        i=i+2
        i=i-2
        l.append("even")
    else:
        l.append("odd")
print(l)
'''
#-------------
'''
l=["even" if i%2==0 else "odd" for i in range(1,11)]
print(l)
'''
#---------------------------------------------

#Tuple
'''
l=[1]
print(id(l))
l.append(2)
print(id(l))
'''
#----
'''
t=()
t=tuple()
t=(1,3,5,3,5,9)
print(type(t))
'''
#-----------
'''
a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
'''
#---------
'''
t1=(1,2)
t2=(3,4)
t3=t1+t2
print(t3)

a=[1,2]
b=[3,5]
print(a+b)
print(a*5)

'''
#-----------
'''
t=tuple(range(1,11))
print(t)
print(t[-1])
print(t[::-1])

for i in t:
    print(i)
'''
#----------------
'''
s={} # creates empty dictionary and not set
print(s)
print(type(s))
s=set()
print(s)
print(type(s))
'''
#-------------
'''
s={1,1,1,1,2,3,3,3,4,5}
print(s)
s={5,90,23,67,1,4}
print(s)
#print(s[0]) indexing slicing not allowed in sets

s.add(25)
print(s)
s.discard(1)
print(s)
s.remove(23)
print(s)
s.discard(1)
print(s)
#s.remove(1)

s1={1,2,3}
s2={2,3,4}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(1 in s1)

s1.update([6,7,8])
print(s1)
s1.update((60,70,80))
print(s1)

s1.update({60,70,80})
print(s1)
'''
#---------------------
'''
d=dict()
print(d)
print(type(d))
d={}
print(d)
print(type(d))
student={
    "Name":"Alice",
    "Course":"DSDA",
    "Marks":100}
print(student)
student["Grade"]="A"
print(student)
student["Name"]="Bingo"
print(student)

print(student["Name"]) # o/p value
print(student.get("Name")) # o/p value

print(student.keys())
print(student.values())
print(student.items())

print(student.pop("Grade"))
print(student)

print(student.popitem())
print(student)

#
print(student.pop("Course"))
student["Courses"]=["Python","Excel","PBI",("A","B")]
print(student)

#
student[("A","B")]={1,1,2,3}
print(student)
#student[["A","B"]]={1,1,2,3}
#print(student)

'''
#----------------
'''
s={(1,2,3),"Apple","April"}
print(s)
'''
#--------------------
'''
t=(24,)
print(t)
print(type(t))

'''
#----------
s='''Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with
the use of significant indentation.[33]
Python is dynamically type-checked and garbage-collected.
It supports multiple programming paradigms, including structured
(particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due
to its comprehensive standard library.[34][35]'''

a=s.split()
#print(a) # ["pyhton","is","a"....]
b=[]
for i in a:
    if "a" in i:
        b.append(i)
print(b)


c=[i for i in a if "a" not in i]
print(c)

d=list(set(c))
print(d)

marks=[("Harry",45),("Jerry",26)]
new_marks=[(i[0].upper(),i[1]+5) for i in marks]
print(new_marks)

#--------------------
#1:1,2:4,3:9,4:16,5:25
d={}
for i in range(1,6):
    d[i]=i**2
print(d)

a=[1,34,56,89,23,90,67]
g={}
for i in a:
    g[i]=i**2
print(g)

f={i:i**2 for i in a}
print(f)































