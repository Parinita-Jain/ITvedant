'''
le=float(input("Enter length : "))
br = float(input("Enter breadth : "))
ar =le*br
print(f"The area of rectangle is : {ar}")
'''
#-------------------
'''
# mutable vs immutable datatypes

a=10
print(f"a : {id(a)}")

b=10
print(f"b : {id(b)}")
a=a+1
print(f"a : {id(a)}")
print(f"b : {id(b)}")
c=11
print(f"a : {id(a)}")
print(f"b : {id(b)}")
print(f"c : {id(c)}")
'''
#--------------------------
'''
# List
l=[] # empty list
print(l)
print(type(l))
l=list() # empty list
print(l)
print(type(l))
l=[1,"ABC",None,True,False]
print(l)
print(type(l))

'''
#-----------------------
'''
l=list(range(10,31,2))
print(l)
m=list(range(10,31,2))
print(m)
print(f"l : {id(l)}")
print(f"m : {id(m)}")
'''
#--------------------
'''
# [51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73,
# 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
l=list(range(51,100,2))
print(l)
print(len(l))
# positive indexing
print(l[0],l[5],l[len(l)-1])
# negtive indexing
print(l[-1],l[-7],l[-len(l)])

# slicing
print(l[0:10:2]) #51, 55,59,63,67
print(l[10::2])
print(l[::2])
print(l[::-1])
'''
#-----------------------
'''
l=[1,"ABC","Apple",123]
print(l)
print(id(l))
l.append("Cherry")
print(l)
print(id(l))
l.append(["Cherry","Right"])
print(l)
l.append("Cherry")
l.extend(["Cherry","Right"])
print(l)
l.insert(1,"HI")
print(l)
l.remove("Cherry") # remove 1st occurence of element
print(l)
l.pop() # remove element from the end
print(l)
l.pop(2) # remove element at a partcular index
print(l)

l=[1,3,4,2,0,5,6,3,2,5]
l.sort()
print(l)
l.reverse()
print(l)

del l
print(l)
'''
#--------------------------------------
'''
l=[1,"ABC","Apple",123]
print(l)
for i in l:
    print(i)

# list of all the even numbers from 0 to 20
l=list(range(0,21,2))
print(l)

#----------
l=[]
for  i in range(0,21,2):
    l.append(i)
print(l)
#-------
l=[]
o=[]
for  i in range(0,21):
    if i%2==0:
        l.append(i)
    else:
        o.append(i)
print(l)
print(o)
'''
#---------------
'''
l=[]
for  i in range(0,21,2):
    l.append(i)
print(l)

m=[i for  i in range(0,21,2)]
print(m)
'''
#-------------------
'''
l=[]
for  i in range(0,21):
    if i%2==0:
        l.append(i)
print(l)

m=[i for  i in range(0,21) if i%2==0 ]
print(m)

'''
#-------------------------------------------
'''
l=[]
for  i in range(0,21):
    if i%2==0:
        l.append("even")
    else:
        l.append("odd")
print(l)

m=["even" if i%2==0 else "odd" for  i in range(0,21)]
print(m)
'''
#-----------------------
'''
#take i/p from user and check whether that number is even or odd
n=int(input("Enter a number"))
if n%2==0:
   print("Even")
else:
    print("Odd")
'''
#-------------------------
'''
s="""Data Science
   is my USP.
   I am very good at it"""
print(s)
k="I am a Data_Scientist"
print(s+k)
print(k*3)
print(k[7])
print(k[12:])
print(k[7:11])
print(len(k))
print('D' in k)
print(k.upper())
print(k.lower())
print(k.capitalize())
print(k.title())
a="      Data Scientist     "
print(a.strip())
print(a.lstrip())
print(a.rstrip())
print(a.replace("Data","Big Data"))
a="      Data ; Scientist     "
print(a.split(" "))
print(a.split(";"))
print(" ; ".join(["Hi","Good Morning","Hello","A334"]))
print(a.find(" "))
print(a.count(" "))
s="Data"# Scientist "#  123456 789Ten  "
s=" A "
print(s,s.isalpha())
print(s,s.isdigit())
print(s,s.isalnum())
print(s,s.isspace())
print(s,s.islower())
print(s,s.isupper())

'''
#----------------
'''
#palindrome
s="racecar"
a="palindrome"
print(a[::])
print(a[::-1])
w=input("Enter a word :")
if w==w[::-1]:
    print("palindrome")
else:
    print("not")
'''
#---------
'''
s="pAlindromE is very interesting"
a=0
for i in s.lower():
    if i in ("a","e","i","o","u"):
        a=a+1
print(a)
        
'''
#--------------------------
emails=["Abc@gmail.com","xyz@outlook.com"]
u=[]
for i in emails:
    print(i)
    q=i.split("@")
    print(q)
    print(type(q))
    u.append(q[0])
print(u)




























