#----- interactive mode------

Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
a
10
b
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    b
NameError: name 'b' is not defined

========================= RESTART: E:/ParinitaJain/Python/demo.py =========================
10

========================= RESTART: E:/ParinitaJain/Python/demo.py =========================
10
20
20
20+30
50
20+60
80
30+60
90
(30+60)*0.01
0.9
A=20
A
20
a
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?
a=10
a
10
A
20
# Case Sensitive



a=20
a
20
A=10
A
10
a
20
A
10
type(a)
<class 'int'>
a="ABC"
type(a)
<class 'str'>
a=10.67
type(a)
<class 'float'>
a=True
type(a)
<class 'bool'>
a
True
a=true
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a="true"
type(a)
<class 'str'>
a="1"
type(a)
<class 'str'>
a*3
'111'
a*10
'1111111111'
type(a)
<class 'str'>
a/10
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a/10
TypeError: unsupported operand type(s) for /: 'str' and 'int'
a=1
a/10
0.1
a=1
b=2
a+b
3
a="1"
b="2"
a+b
'12'
a
'1'
a1=200
1a=200
SyntaxError: invalid decimal literal
a15421436568780689=90
15421436568780689a=40
SyntaxError: invalid decimal literal
_a=10
a_=20
a@=10
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a@=10
TypeError: unsupported operand type(s) for @=: 'str' and 'int'
a.=10
SyntaxError: invalid syntax
a#10
'1'
a*10
'1111111111'
a#526578
'1'
a=b=c=10
a
10
b
10
c
10
a,b,c=1,3,5
a
1
b
3
c
5
a=[7+5-9*8]
a
[-60]
a=[7+\
   5\
   -9\
   *8]
a
[-60]
#fgfghfghh
fghfghgjh
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    fghfghgjh
NameError: name 'fghfghgjh' is not defined
a=fghfghgjh
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a=fghfghgjh
NameError: name 'fghfghgjh' is not defined
"fghfghgjh"
'fghfghgjh'
1
1
'fghfghgjh'
'fghfghgjh'
'fghfghgjh"
SyntaxError: unterminated string literal (detected at line 1)
#yuiyti,jhhmh hihg hjn rt
'''
this
is
an example
of
multiline
comment
'''
'\nthis\nis\nan example\nof\nmultiline\ncomment\n'
"""this\nis\nexample"""
'this\nis\nexample'
a
[-60]
b
3
a\nb
SyntaxError: unexpected character after line continuation character
print(a)
[-60]
print(a,"\n",b)
[-60] 
 3
>>> print("a\nb")
a
b
>>> a=10
>>> b=5
>>> a+b
15
>>> a-b
5
>>> a*b
50
>>> a/b
2.0
>>> a^b
15
>>> a**b
100000
>>> 15
15
>>> a**b
100000
>>> a//b
2


#--------- class 1---
'''
l=int(input("Enter length : "))
b=int(input("Enter breadth : "))
print("Area of rectangle is : ",l*b)

'''
#--------------
'''
r=int(input("Enter radius : "))
print("Area of circle is : ",3.14*(r**2)) #3.14*r*r
'''
#-------
'''
l=int(input("Enter length : "))
b=int(input("Enter breadth : "))
c=l
l=b
b=c
print(f"The swapped values are : {l} , {b}")

'''
#--------------
'''
n=int(input("Enter number : "))
if(n%2==0):
    print("Number is even")
else:
    print("Number is odd")
'''
#--------------

n=int(input("Enter number : "))
if((n%3==3)and(n%5==0)):
    print("Number divisible by both 3 and 5")
elif((n%3==0)and(n%5!=0)):
    print("Number divisible by 3 and not by 5")
elif((n%5==0)and(n%3!=0)):
    print("Number divisible not by 3 and only by 5")
else:
    print("Number not divisible by both 3 and 5")
print("The end of prog")    

#--------- class 2---
'''
ch=int(input("""Enter choice :
                1. Simple Interest Calculation
                2. Compound Interest Calculation
                3. Age comparison :\n"""))

if(ch==1):
    #si=(p*r*t)/100
    p=int(input("Enter the value of Principle : "))
    r=int(input("Enter the value of Rate : "))
    t=int(input("Enter the value of Time : "))
    si=(p*r*t)/100
    print("The simple interest is : ",si)
elif(ch==2):
    #ci=p*(1+(r/100))**t
    p=int(input("Enter the value of Principle : "))
    r=int(input("Enter the value of Rate : "))
    t=int(input("Enter the value of Time : "))
    ci=int((p*(1+(r/100))**t)-p)
    print("The compound interest is : ",ci)
elif(ch==3):
    # 2 input-- age1 and age 2
    age1=int(input("Enter Age1: "))
    age2=int(input("Enter Age2: "))
    if(age1>age2):
        print("Age1 is greater ")
    else:
        print("Age2 is greater ")
else:
    print("Enter correct choice.")
        
'''
#----------
#Immutable datatypes--eg:- strings, tuples,integers,floats,booleans
'''
Immutable
'''
'''
a=1
print(a)
print(id(a))
a=2
print(a)
print(id(a))
b=2
print(b)
print(id(b))
c=2
print(c) 
print(id(c))
a=3
print(a)
print(id(a))
'''
a="Hello"
print(a)
print(id(a))
a=a+" World , " # conatenation
print(a)
print(id(a))

a=a*3 # repetition
print(a)
print(id(a))

a="Good Morning, India !"
print(a[0]) # indexing
print(a[5])
print(a[-1])
print(a[-3])

a="Good Morning, India !"
print(a[0:8]) # slicing-- [starting_index:stopping_index] --> stopping_index-1
print(a[5:12])
print(a[-5:])
print(a[-7:-2])
print(a[:])
print(a[1::2])

print(a[::-1])

print(a[::])

w="3" #input("Enter a word : ")
if(w[::]==w[::-1]):
    print("Its a palindrome")
else:
    print("Its's not a palindrome")


a="1234"
a=str(a)
print(a[-1])

a=" Hello "
print(a.upper())
print(a.lower())
print(len(a))
print(a.strip())
print(a.replace("Hello","Good Morning"))
a="Hello World"
print(a.split())
print(a.find("Hello"))
print(a.find("Python"))
print(a.count("o"))
print(a.startswith("Hello"))
print(a.endswith("i"))

#----------
#mutable objects-- list,set,dictionary
#---------

'''
vowels="aeiouAEIOU"
x="a"
if x not in vowels:
    print("Consonants")
else:
    print("vowel")
'''
#-------------
'''
if (x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or
    x=="A" or x=="E" or x=="I" or x=="O" or x=="U"):
    print("Vowel")
else:
    print("Not vowel")
'''
#-------------------
'''
a=9
b=70
c=300
if((a>b) and (a>c)):
    print("Greatest no. : ",a)
elif((b>a)and (b>c)):
    print("Greatest no. : ",b)
else:
    print("Greatest no. : ",c)
'''  
#---------------------
'''
s="Good morning Everyone"
print(s.index("o")) #

#s="10"
#s="abc10"
s="&"
print(s.isnumeric())
print(s.isalpha())
print(s.isalnum())
'''
#-------------
'''
li=[1,2,3]
print(type(li))

el=[]
print(type(el))

e=list()
print(type(e))



li=[1,"Apple",23.0,True,[45,"April",34,89,"ABCD"]] # 
print(type(li))
print(li)

print(li[2])
print(li[1:4])

s="Good Morning Everyone !"
print(s[5:12])

l=["Z","X","Y"]
x=li+l
print(x)

y=l*3
print(y)

g=s.split()
print(type(g))
print(g)

li=[1,"Apple",23.0,True,[45,"April",34,89,"ABCD"]] #
print(li[4][1:4])

print(len(li))

print(id(li)) #2238163732928

li.append(9)
print(li)
print(len(li))
print(id(li)) #2974673882304

l3=[1,"Apple",23.0,True,[45,"April",34,89,"ABCD"]]
print(id(l3))

li.append(["p","q","r"])
print(li)

li.extend(["p","q","r"])
print(li)

li.insert(0,"Good Morning")
print(li)

li.remove(1)
print(li)


li=[1,"Apple",23.0,True,[45,"April",34,89,"ABCD"]]
x=li.remove(23.0) #
print(x)
print(li)

y=li.pop(1)
print(y)
print(li)

li.clear()
print(li)

li=[1,2,2,2,3,1,3]
print(li.index(2))

print(li.count(2))

print(li[::-1])

li=[1,2,3,4,5,6,7,8,9]
l=li[1::2]
print(sum(li[1::2]))
print(len(li[1::2]))

l1=[1,2,3]
l2=l1.copy()

print(l2)
l2.append(5)
l1.append(50)
print(l1)
print(l2)

l1=[1,2,3]
l2=l1

print(l2)
l2.append(5)
print(l1)
print(l2)
l2[0]=25
print(l1)
print(l2)
'''
#print(1**3+5**3+3**3) #153

#Anagrams-- listen-- silent
'''
l=[3,45,67,89,90,23,1,2,3,4]
l.sort()
print(l)
l.reverse()
print(l)

l=[67,45,23,9000,23,1,67,78,56]
l.sort()
print(l)
print(l[-2]+l[1])

'''

#-------------------------------
'''
l1=[1,2,[3,4]]
print(l1[2][0])
l1[2][0]=99
print(l1)

l2=l1
print(l1)
print(l2)
print(id(l1))
print(id(l2))
l1[0]=100
print("-------- l1[0]=100 ------")
print(l1)
print(l2)
print(id(l1))
print(id(l2))
print("-------- l2[0]=10 -------")
l2[0]=10
print(l1)
print(l2)
print(id(l1))
print(id(l2))
#------------------------------

print("####################################")
l1=[1,2,[3,4]]
#l2=l1.copy()
import copy
l2=copy.deepcopy(l1)
print(l1)
print(l2)
print(id(l1))
print(id(l2))
l1[0]=100
print("-------- l1[0]=100 ------")
print(l1)
print(l2)
print(id(l1))
print(id(l2))
print("-------- l2[0]=10 -------")
l2[0]=10
print(l1)
print(l2)
print(id(l1))
print(id(l2))

'''
#-----------------------
# tuples
'''
t1=(1,2,3)
print(t1)
print(type(t1))
t1=(1,)
print(t1)
print(type(t1))
l1=[1]
print(l1)
print(type(l1))
l1=[1]
#t1.append(4)

t1=(1,2,3)
print(t1[0])
print(t1[:])
print(t1*3)
print(t1)
print(len(t1))
print(t1.count(1))
l=[1,2,3,4,1,2,3,4,1,2,3,4]
t2=tuple(l)
print(t2)
l3=list(t2)
print(l3)
'''
#-----------------
#--sets
'''
s={1,2,1,2,3,4,1,2,3}
print(s)
print(type(s))
l=[1,2,3,1,2,3,4,5]
s1=set(l)
print(s1)
s1={7,6,90,45,23,67}
print(s1)

s1.add(1)
print(s1)
s1.remove(6)
print(s1)
#s1.remove(60)
print(s1)
s1.discard(60)
print(s1)
a=s1.pop()
print(s1)
print(a)

s1={1,2,3}
s2={2,3,4}
s3=s1.union(s2) #  s1|s2
print(s3)
s4=s1.intersection(s2) # s1&s2
print(s4)
s5=s1.difference(s2) # s1-s2
print(s5)
s6=s1.symmetric_difference(s2) # s1^s2
print(s6)

s7={10,20}
print(s7.issubset(s1))
print(s7.issuperset(s1))
print(s7.isdisjoint(s1))
'''
#=========================
# Dictionary----------------
'''
d={1:["Ariel,April,23"],
   2:["Harry","Potter",25],
   3:["Ariel,April,23"]}
print(d)
print(d[1])
d[4]=56
d["a"]=94.6
print(d)
d[(1,2,3,4)]=(7,8,9)
print(d)
print(len(d))
print(d.keys()) # keys() gives dictionary keys as o/p
print(d.values())
print(d.items())
d[1]="Hello"
d[1]="Good Morning"
print(d)
d[78.9]=45
print(d)
#d[[1,2]]=[78,90,45.6]
print(d)
'''
'''
d={"a":1,"b":2,"c":3}
print(d.get("b")) # d={key:value}
x=d.pop("c")
print(d)
print(x)
d["c"]=3
d["d"]=4
print(d)
print("----------------------")
print(d)
x=d.popitem()
print("After 1st popitem : ")
print(d)
print(x)
print(type(x))
y=d.popitem()
print("After 2nd popitem : ")
print(d)
print(y)
print(type(y))

#---------------
print("-----------------")
d1={}
print(type(d1))
s={1.1,}
print(type(s))
s1=set()
print(type(s1))
d=dict()
print(type(d))
t=tuple()
print(type(t))
l=list()
print(type(l))

#--------------------------
print("---------------------------")
d1={1:1,2:4,3:9}
d2={4:16,5:25,6:36}
d1.update(d2)
print(d1)
d1={1:100,2:200,3:300}
d2={1:10,2:20,3:30}
d1.update(d2)
print(d1)
d1.clear()
print(d1)
'''
#----------------------------
print("-----------------------")
'''
print(range(10))
print(list(range(10)))#list()->0,1,2.......9
print(list(range(2,21,2))) # start_index,stop_index,jump -?-- 2,4,6....20
l=list(range(20,1,-2))
print(l)
'''
# for variable in iterable:
'''
l=list(range(1,11))
for i in l:
    print(i," * 1 = ",i)

for i in range(2,21,2):
    print(i)

l=["Harry","Potter","Tom","Bob"]
for i in l:
    print(i)

d={1:1,2:4,3:9,4:16}
for i in d:
    print(d[i])
'''
'''
s=0
for i in range(6):
    print(s,"  +  ",i)
    s+=i #s=s+i
    print("Intermediate Sum : ",s)
print(s)

'''
#------------------------
'''
l=[]
s=0
n=int(input("How many times do u want to enter number :"))
for i in range(n):
    l.append(int(input("Enter a number : ")))

for i in l:
    s=s+i
    if(i%2==1):
        print(f"number {i} is odd")
    else:
        print(f"number {i} is even")
print("The number u enterd are : ",l)
print("the sum of numbers in list are : ",sum(l))
print(f"The total sum of entered numbers are : {s}")

'''
#-------------
'''
n=int(input("Enter number > 1 : "))
m=1
for i in range(n,0,-1):
    m=m*i
print("The factorial of number is : ",m)
m=1  
for i in range(1,n+1):
    m=m*i
print("The factorial of number is : ",m)

'''
#-----------------------------------
'''
for i in range(1,5):
    print("*"*i)

for i in range(4,0,-1):
    print("*"*i)

a="Hello"*3
print(a)

for i in range(1,5): # 1,2,3,4
    print(" "*(4-i),end="") #,end=""
    print("* "*i)
'''
#------
'''
i=1
while(i<6):
    print(i)
    #i=i+1
    
'''
#--------------
'''
i=1
while(i<=10):
    print(f"2 * {i} = {2*i}")
    i=i+1
print("Outside loop statement")

'''
#----------------

# Control flow statements -- pass, continue, break
'''
print("For loop - Pass")
for i in range(5):
    if i==2:
        pass
    print(i)
print("Outside loop statement")

print("While loop - Pass")
i=0
while i<5:
    if(i==2):
        pass
    print(i)
    i=i+1
print("Outside loop statement")

'''
'''
print("For loop - Pass")
for i in range(1,6):
    if i==2:
        print("Before continue")
        continue
        print("After continue")
    print(i)
print("Outside loop statement")

print("While loop - Pass")
i=0
while i<5:
    i=i+1
    if(i==2):
        continue
    print(i)
print("Outside loop statement")

'''
'''
print("For loop - break")
for i in range(1,6):
    if i==2:
        print("Before break")
        break
        print("After break")
    print(i)
print("Outside loop statement")

print("While loop - Pass")
i=0
while i<5:
    i=i+1
    if(i==2):
        break
    print(i)
print("Outside loop statement")

'''
'''
print("For loop - Pass")
for i in range(1,6):
    if i==2:
        print("Before continue")
        continue
        print("After continue")
    print(i)
else:
    print("In else part of loop")
print("Outside loop statement")

print("While loop - Pass")
i=0
while i<5:
    i=i+1
    if(i==2):
        continue
    print(i)
else:
    print("In else part of loop")
print("Outside loop statement")

print("---------else-break----------")

print("For loop - Pass")
for i in range(1,6):
    if i==2:
        print("Before break")
        break
        print("After break")
    print(i)
else:
    print("In else part of loop")
print("Outside loop statement")

print("While loop - Pass")
i=0
while i<5:
    i=i+1
    if(i==2):
        break
    print(i)
else:
    print("In else part of loop")
print("Outside loop statement")

'''
'''
# prime number
n=int(input("enter any number : "))
for i in range(2,n):
    if(n%i==0):
        print("Number not prime")
        break
else:
    print("Number is prime")
print("Outside loop")

'''
'''
l=list(range(1,6))
l1=[]
for i in l:
    l1.append(i**2)
print(l1)

l2=[]
for i in range(2,7,2):
    l2.append(i**2)
print(l2)
    
print("---- List Comprehension -----")

l3=[i**2 for i in range(2,7,2)]
print(l3)

l=list(range(1,6))
l4=[i**2 for i in l]
print(l4)

'''
'''
l1=[]
for i in range(1,11):
    if i%2==0:
        l1.append(i)
print(l1)

print("----------- lc --------")
l=[i for i in range(1,11)if i%2==0 ]
print(l)

l=["harry","tom","bob","marley"]
l2=[i.upper() for i in l]
print(l2)

l3=[i for i in l if i not in ("bob","tom")]


print(l3)

l4=[len(i) for i in l if i not in ("bob","tom")]
print(l4)

print("-------- dictionary comprehension-----")
d1={i:len(i) for i in l if i not in ("bob","tom")}
print(d1)
'''
#---------Nested loop--------- Pattern printing
# wed thur fri no class--but do self learning assignment assessment strictly
# i hope my message reached
# present ur project
'''
for i in range(1,3):
    for j in range(1,3):
        print(j,end="")
    print()

for i in range(1,3):
    for j in range(1,3):
        print(j,i)



for i in range(1,6):
    print("i : ",i)
    for j in range(1,6):
        print(j,end="")
        print("Inner Loop")
    print("Outside Inner Loop") # end="\n"
    print("This is the part of outside loop")



for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("-----Second loop-----")
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
  
print("-----Third loop-----")
for i in range(1,6):
    for j in range(1,6):
        print(i,j," ",end="")
    print()

val=65
for i in range(5):
    print(chr(val))
    val=val+1

val=65
for i in range(5):
    print(chr(val),end="")
    val=val+1
'''
#-----------------
'''
val=65
for i in range(5):
    for j in range(5):
        print(chr(val),end="")
        val=val+1
    print("\nValue of val Before change: ",val)
    val=65
    print("Value of val After change: ",val)
    print()

'''
#---------------------
#--------- Functions -------------
'''
print()
input()
abs()
int()
list()
set()
dict()
'''
'''
print("Hello World !")

val=ord('a')
print(val)
print(type(val))

'''
#---------------
'''
a,b=1,2
c=a+b
print(f"Addition of {a} and {b} is {c}")
'''
#----
# 1st way---
'''
# function without arguments
def addition():
    a,b=1,2
    c=a+b
    print(f"Addition of {a} and {b} is {c}")
    
addition()

'''
#---
'''
#2nd way
#function with arguments
def addition(x,y):
    c=x+y
    print(f"Addition of {x} and {y} is {c}")
# function def with default parameters
def subtraction(y,x=0): 
    print(f"x : {x} and y : {y}")
    c=x-y
    print(f"Subtraction of {x} and {y} is {c}")
    return
    
def multiplication(a,b):
    c=a*b
    return c
    
def taking_input():
    x=int(input("Enter a number : "))
    y=int(input("Enter another number : "))
    return x,y
    
def division(u=1,v=1):
    #print(f"The division of 2 nos is  : {u//v}")
    return u//v

#addition(4,5)
#subtraction(1)
x=4
y=5
m=0
m=multiplication(x,y)
print(f"Multiplication of {x} and {y} is {m}")
a,b=taking_input()
r=division(a,b)
print(f"Division of {a} and {b} is {r}")
print(print("Hi"))

'''
#---------------------
'''
def even_odd(li):
    print(li)
    for i in li:
        if(i%2==0):
            print(f"{i} is even")
        else:
            print(f"{i} is odd")   

l=[12,45,20,9,13,10,65,79,82,25]
even_odd(l)
'''
#-----------
#variable length arguments *args and **kwargs
'''
def even_odd(*li):
    print(li)
    print(type(li))
    for i in li:
        if(i%2==0):
            print(f"{i} is even")
        else:
            print(f"{i} is odd")   

#l=[12,45,20,9,13,10,65,79,82,25]
even_odd(12,45,20,9,13)
'''
'''
def v_kw_args(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i in kwargs.keys():
        print(i)
    for i in kwargs.values():
        print(i)
    for i in kwargs.items():
        print(i)

v_kw_args(english=80,hindi=90,maths=91,history=85)

'''
#--------------------
#Built-in functions
#nums=[5,4,6,3,6]
#print(min(nums),max(nums),sum(nums),len(nums))

'''
l=['a','v','e']
print("l ",l)
print("Sorted ",sorted(l))
print("l ",l)
print("Reversed ",reversed(l))
l=list(reversed(l))
print("l ",l)
l.sort()
print("l ",l)
'''
#---
'''
marks={"Harry":78,"Tom":98,"Jerry":89,"Bella":56}
print(sorted(marks.values()))
print(list(reversed(marks.values())))
'''
#---
'''
names=["Harry","Tom","Jerry","Bella"]
marks=(78,98,89,56)
age=[20,21,20,21]
print(list(zip(names,marks,age)))
print(tuple(zip(names,marks,age)))
print(dict(zip(names,marks)))
'''
#------
'''
a=2
c=a*a # a**2

def fun(b):
    return b*b
print(fun(2))

a=1
b=2
c=a+b
def fun1(x,y):
    return x+y
print(fun1(a,b))
'''   
#--- lambda function ---
'''
fun = lambda b : b*b
print(fun(2))

fun1 = lambda x,y:x+y
print(fun1(2,3))


def g(x,y):
    if x>y:
        return x
    else:
        return y
print(g(2,3))

g=lambda x,y :x if x>y else y
print(g(2,78))
'''
'''
def e_o(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
print(e_o(25))

e_o = lambda x:"even" if x%2==0 else "odd"
print(e_o(40))

'''
'''
dby3= lambda x:True if x%3==0 else False
print(dby3(7))

l=[12,34,23,45,67,22,10,15,32,41]
print(list(filter(dby3,l)))

'''
'''
def prime_f(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True

l=[12,34,23,45,67,22,10,15,32,41]
print(list(filter(prime_f,l)))

'''
'''
m=lambda a:a**2
l=[2,4,3,4,7,2,1,5,2,1]
print(list(map(m,l)))

'''
#-----------------------------
'''
def p(x):
    y=str(x)
    if y[::]==y[::-1]:
        return True
    else:
        return False
l=[171,1222,12321,1,216621,823]
print(list(filter(p,l)))
'''
#-----------------
'''
def fun(n):
    print("In fun function, called from first")
    print(n)
    print("returnng to point of call i.e. first function")
    return "Good Morning"

def second(g):
    print("In second function, called from first()")
    print(g)
    print("returnng to point of call i.e. first function")

def first(x):
    a=input("Enter your name : ")
    print("Hi ")
    r=first(a)
    print("In first function, returned from second()")
    second(r)
    print("In first function, returned from second()")
    return "Final return to point of call"

print("Doing a function call to first")
a=first(5)
print(a)

'''
#------------------------
'''
def f(n):
    s=0
    for i in range(n,0,-1):
        s=s+i
    return s
print(f(5))
'''
#--------------------
'''
# recursion function
def a(x):
    if x==0:
        return 0
    else:
        return x+a(x-1)

print(a(5))

#-------------------------
def a(x):
    if x==1:
        return 1
    else:
        return x*a(x-1)

print(a(5))

#---------------------
def countdown(x):
    print(x)
    if(x==1):
        return 0
    else:
        return countdown(x-1)

print(countdown(5))

'''
#---------------------
#Armstrong number:
'''
def f(number):
    num_str=str(number)
    num_length=len(num_str)
    sum_of_powers=sum(int(digit)**num_length for digit in num_str)
    return sum_of_powers==number
number=153 #123
if f(number):
    print("Yes")
else:
    print("No")

#1**3+5**3+3**3 == 153
'''

#------------------------------
# classwork3.py
'''
class vehicle:
    def assign(self,v_name,v_mode):
        self.name=v_name
        self.mode=v_mode
    def display(self):
        print(f"{self.name} and {self.mode}")

v1=vehicle()
v1.assign("Car","Land")
v1.display()
print(type(v1))
print(v1.name)

v2=vehicle()
v2.assign("Ship","Water")
print(type(v1))

v3=vehicle()
v3.assign("Airplan","Air")
print(type(v3))

v4=vehicle()
v4.assign("taxi","road")
v4.display()
'''
# constructor method : __init__
'''
class vehicle:
    def __init__(self,v_name,v_mode):
        print("By default constructor method call ho jaega")
        self.name=v_name
        self.mode=v_mode
    def display(self):
        print(f"{self.name} and {self.mode}")

v1=vehicle("taxi","road")
v1.display()

'''
#------- class attribute


#----------------
'''
#__str__() converts objects into string
#__del__() - destructor
class vehicle:
    def __init__(self,v_name,v_mode):
        print("By default constructor method call ho jaega")
        self.name=v_name
        self.mode=v_mode
    def __str__(self):
        return f"{self.name} and {self.mode}"
    def __del__(self):
        print("Object deleted")
    

v1=vehicle("taxi","road")
print(v1)
del v1
#print(v1)
'''
#-------------
#Multilevel inheritance
'''
class grandfather:        
    def gfp(self):
        self.p1="Castle"
        return "Castle"

class father(grandfather):
    def fp(self):
        self.p2="Penthouse"
        return "Penthouse"

class you(father):
    def __init__(self):
        self.p3="Land on moon"
    def display(self):
        print(f"""I have my :
                  Grand Father's property {self.gfp()},
                  Father's property {self.fp()},
                  My property {self.p3}""")

me=you()
me.display()

'''
'''
#single level inheritance

class parent:
    def display(self):
        print("Parent class")

class child(parent):
    pass

ch=child()
ch.display()

'''
#Multiple inheritance-- many parents , single child
'''
class father:
    def father(self):
        print("father function")
class mother:
    def mother(self):
        print("mother function")

class child(father,mother):
    def child(self):
        father.father(self)
        mother.mother(self)
        print("child class")
        
ch=child()
ch.child()
'''
#------------------
'''
class father:
    def father(self):
        print("father function")
    def display(self):
        print("Father display method")
class mother:
    def mother(self):
        print("mother function")
    def display(self):
        print("Mother display method")

class child(father,mother):
    def child(self):
        father.father(self)
        mother.mother(self)
        print("child class")
    def display(self):
        #super().display()
        father.display(self)
        mother.display(self)
        print("Child display method")
    
        
ch=child()
ch.child()
ch.display()

'''
#hierarchical inheritance -- 1 parent, many child
''''
class shape:
    def display(self):
        print("Shape class")
class square(shape):
    pass

class circle(shape):
    pass

sq=square()
sq.display()

ci=circle()
ci.display()

'''
#Polymorphism --
# method overriding
''''
class animal:
    def sound(self):
        return "Some generic sound"

class horse(animal):
    def sound(self):
        return "Horse sound"

class elephant(animal):
    def sound(self):
        return "Elephant sound"

def animal_sound(ani : animal):
    print(type(ani))
    print(ani.sound())

h=horse()
animal_sound(h)
e=elephant()
animal_sound(e)
'''
'''
'''
#method overloading
'''
class addi:
    
    def adding(self,a,b):
        return a+b
    def adding(self,a,b,c):
        return a+b+c
    
    def adding(self,a,b,c=0,d=0):
        return a+b+c+d
    def adding_args(self,*args):
        print(type(args))
        print(args)
        return sum(args)

a=addi()
print(a.adding(2,3,3,4))
print(a.adding_args(2,3,3,4,2,2,3,4,5,6))
'''
'''
#Abstract base class and Abstract methods--

from abc import ABC,abstractmethod

class animal:
    @abstractmethod
    def sound(self):
        pass
class horse(animal):
    def sound(self):
        return "neigh"
class elephant(animal):
    def sound(self):
        return "trumpet"

a=horse()
print(a.sound())
a=elephant()
print(a.sound())
'''
#--------------------------------------------------
# file handling
'''
f=open("test.txt")
print(f.tell()) # start of file
print(f.read())
print(f.tell()) # end of file
print(f.seek(4))
print(f.read())
print(f.tell())

'''
'''
f=open("test.txt")
text=f.readline() #
while(text):
    print(text)
    text=f.readline()

print(f.tell())
f.seek(0)
print(f.readlines())

'''
'a' 'x' 'b' 't' '+'
'''
import shutil
shutil.copyfile("test.txt","copied.txt")
print("file copied successfully")
'''
'''
f=open("test.txt","w")
f.write("Hi this is a write mode")
f.close()
#print(f.read())
f=open("test.txt","a")
f.write("Hi this is a append mode")
f.close()

'''
#-------------
'''
class action:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def swap(self):
        print("Before swapping : ",self.a,self.b)
        self.a,self.b=self.b,self.a
        print("After swapping : ",self.a,self.b)

obj1=action(300,400)
obj1.swap()
'''
#-----------------------
'''
f=open("test.txt","w")
f.write("Hi this is a write mode")
f.close()
'''
'''
with open("test.txt","a") as f:
    f.write("Hi this is a write mode with with Some chnages something")

'''
#r+,w+,a+
'''
with open("test1.txt","a+") as f:
    f.write("Hi this is a append+ mode with with Some chnages something")
    f.seek(0)
    print(f.read())

'''
'''
with open("test2.txt","r+") as f:
    f.write("Hi this is a read+ mode with with Some chnages something")
    f.seek(0)
    print(f.read())
'''
'''
with open("test.txt","w+") as f:
    f.write("Hi this is a write+ mode with with Some chnages something")
    f.seek(0)
    print(f.read())

'''
'''
with open("test2.txt","wt+") as f:
    a="[1,2,3,4]"
    f.write(l)

'''
'''
#b
import pickle

num=[1,2,3,4,5]
with open("test.txt","wb+") as f:
    #pickling/serialization
    num_se=pickle.dumps(num)
    print(type(num_se))
    print(num_se)
    f.write(num_se)
    
    f.seek(0)


    #unpickling/deserialization
    r=f.read()
    print(r)
    l=pickle.loads(r)
    print(l)
    print(type(l))

'''
#------------------
'''
class vehicle:
    c="white"
    def __init__(self,name,speed,mileage):
        self.speed=speed
        self.name=name
        self.mileage=mileage
    def show(self):
        print("Color : ",vehicle.c)
        print("Name : ",self.name)
        print("Speed : ",self.speed)
        print("Mileage : ",self.mileage)


s_v=vehicle("School volvo",180,12)
A_Q5 = vehicle("Audi Q5", 240,18)

s_v.show()
A_Q5.show()
'''

































        














    

















