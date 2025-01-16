"""
12345
12345
12345
12345

no. of rows=4
no of cols = 5
"""
'''
for i in range(1,5):
    for j in range(1,6):
        print(j,end=" ")
    print()
'''
#-----------------------------
"""
a="I am a Robot"
count number of vowels
vowel="aeiouAEIOU"
"""
'''
v="aeiouAEIOU"
s="Yash"
su=0
for i in s:
    if i in v:
        su=su+1
print(f"Total number of vowels : {su}")
'''
#------------------
"""
a=2
b=3
print(f"Before swapping : a:{a} b:{b}")
c=a
a=b
b=c
print(f"After swapping : a:{a} b:{b}")
"""
'''
a=2
b=3
print(f"Before swapping : a:{a} b:{b}")
b,a=a,b
print(f"After swapping : a:{a} b:{b}")
'''
#-------------------
# List--
'''
l=[]
print(type(l))
print(l)
m=list()
print(type(m))
print(m)
l=[1,"A",None,True,"Apple","April","Autumn","Santa Claus",45.78,90]
print(type(l))
print(l)
print(l[0],l[-1],l[-2])#indexing
print(l[4:8])

m=list(range(1,51,2))
print(m)

m=[1,2,3]
print("m-------\n",id(m))
print(m)
print(id(m))

n=[1,2,3]
print("n-------\n",id(n))
print(n)
print(id(n))

m[0]="Apple"
print(m)
# append
m.append(1234)
print(m)
m.extend([89,78,67,45]) 
print(m)
m.append([800,7800,6700,4500])
print(m)
#['Apple', 2, 3, 1234, 89, 78, 67, 45, [800, 7800, 6700, 4500]]
print(m[8][1])
print(m[-1][-3]) # single value access
m.insert(2,"Elephant")#----------
print(m)

for i in m:
    print(i)

l=["One",2,3,2,3,"One",4]
l.remove("One")
print(l)
c=l.pop()
print(c)
print(l)
c=l.pop()
print(c)
print(l)
print(l.count(3))
print(sum(l))
l.sort()
print(l)
l.reverse()
print(l)

#---
"""
l=[1,4,9,16,25,36,49,64,81,100]-- this is want
m=[1,2,3,4,5,6,7,8,9,10]-- this i have
"""
l=[]
for i in range(1,11):
    l.append(i**2)
print(l)

ll=[i**2 for i in range(1,11)] # list comprehension
print(ll)

#--------
l=[]
for i in range(1,11):
    if i==7:
        l.append("Hello")
    else:
        l.append(i**2)
print(l)

l=["Hello" for i in range(1,11) if(i==7)]
print(l)

l=["Hello" if(i==7) else (i**2) for i in range(1,11)]
print(l)

'''
#----------
'''
l=["april","autumn","bob","tom"]
l1=[i.upper() for i in l] # list comprehension
l2=[i for i in l if "o" in i]
print(l1)
print(l2)
l1=[]
for i in l:
    l1.append(i.upper())
print(l1)
l2=[]
for i in l:
    if "o" in i:
        l2.append(i)
print(l2)

'''
#-----------------
'''
t=()
print(type(t))
t=tuple()
print(type(t))
t=(1,"Abnbvj",None,True)
print(type(t))
print(t)
print(t[0]) # indexing
t=tuple(range(1,51))
print(t)
print(t[5::2])# slicing
#t[0]=100
#print(t)
print(len(t))
t=(1,1,1,1,1,2,3,2,3,4)
print(t.count(1))

'''
#---------------------------
# sets--
#s={}
'''
s=set()
print(type(s))
t=(1,)
print(type(t))
s={1,1,1,1,1,2,3,2,3,4}
print(type(s))
print(s)
s={45,23,12,"Apple","Banana"}
print(s)
#print(s[0])-- cant do indexing slicing
s.add(True)
print(s)
s.remove(23)
print(s)
#s.remove(23) -- error
s.discard(23)
print(s)
a=s.pop()
print(a)
print(s)

s1={1,2,3}
s2={2,3,4}
print(s1.union(s2))#s1|s2
print(s1.intersection(s2)) # s1&s2
print(s1.difference(s2))#s1-s2
print(s1.symmetric_difference(s2))#s1^s2

print(s1|s2)
s3={10,20}
print(s3.issubset(s1))
print(s3.issuperset(s1))
print(s3.isdisjoint(s1))

'''
# Dictionary
'''
d={}
print(d)
print(type(d))
d=dict()
print(d)
print(type(d))
d={
    "Name":["Tom","Jerry","Bob","Harry"],
    (1,2,3,90):[45,True],
    34.67:"abcd"}
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d["Name"])
d["Name"]="April"
print(d)
print(d["Name"])
print(d.get("Name"))
y=d[34.67]
print(y)
x=d.pop(34.67)
print("x",x)
print(d)
d[34]=y
print(d)
x=d.popitem()
print(x)
print(d)
x=d.popitem()
print(x)
print(d)

d1={1:1,2:4,3:9}
d2={4:16,5:25}
d1.update(d2)
print(d1)

#
t=(1,1,1,1,2,3,2,3,2,3,7)
t=tuple(set(t))
print(t)
'''
#---------
'''
l=[]
for i in range(1,51):
    #print(i)
    l.append(i)
print(l)

'''
'''
l=list(range(1,51))
print(l)
for i in l:
    if i%2!=0:
        if i==7:
            print("Hello")
        else:
            print(i)

# whether the given number is prime or not
# give all the prime numbers between 1 to 100
'''
# dictionary comprehension
#d={1:1,2:4,3:9}
d={}
for i in range(1,6):
    d[i]=i**2
print(d)

d={i:i**2 for i in range(1,6)}
print(d)


































































