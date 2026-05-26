'''
a=300
b=53
print(f"Before swapping : {a} {b}")
c=a
a=b
b=c
print(f"After swapping : {a} {b}")
'''
#----------------------------------
'''
a=0
b=1
print(f"{a} , {b}",end=" , ")
for i in range(2,13):
    s=a+b
    print(f"{s}",end=" , ")
    a=b
    b=s
'''
#---------------------
'''
a=0
b=1
n=int(input("Enter number of terms of fibonacci series : "))
print(f"{a} , {b}",end=" , ")
for i in range(2,n):
    s=a+b
    print(f"{s}",end=" , ")
    a=b
    b=s

'''
#------------------
'''
a="65"
print(type(a))
b=str(int(a)+1)
print(type(b))
print(b)
print(chr(int(b)))

a="67"
print(chr(int("97")))

'''
#-------------------
'''
a="?"
b=a*5
print(b)

'''
#--------------------
'''
n=153
m=str(n)
for i in m:
    print(f"{m} {type(m)}")
for i in range(len(m)):
    print(f"{m[i]} {type(m[i])}")
    
a="Hello World"
print(len(a)) # 11
for i in range(len(a)):
  print(a[i],end="")

'''
#-----------------
'''
n=9474
a=len(str(n)) # a=3
print(a)
s=0
b=str(n)
for i in range(a):
    s=s+int(b[i])**a
    print(s)
if s==n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    
'''
#-----------------------------
'''
n=int(input("Enter number : "))
if n%11==0:
    print(f"{n} divisible by 11")
'''
#--------------------
'''
n=int(input("Enter number : "))
if n%19==0:
    print(f"{n} divisible by 19")
else:
    print(f"Remainder is {n%19}")

'''
#-------------------

n=int(input("Enter number : "))
for i in range(2,n):
    if n%i==0:
        print(f"{n} not prime")
        break
else:
    print(f"{n} is prime")
print("Outside statement")































    
