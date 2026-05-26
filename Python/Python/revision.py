'''
num=int(input("Enter a number : "))
if num<0:
    print("Factorial is not defined for negative numbers")
elif num==0:
    print("Factorial of 0 is 1.")
else:
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)
'''
#----------------------
'''
# palindrome
n=input("Enter word or number  : ")
if n[::]==n[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
#---------------------
'''
n=input("Enter word or number  : ")
print(n[::-1])
print(n[::1])
'''
#---------------------
'''
#Prime number:
num= int(input("Enter a number:"))
if num<0 or num==0:
    print(f"{num} not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} not prime")
            break
    else:
        print(f"{num} is prime")

'''
#---------------------------------------------
'''
# swapping
a="V"
b="S"
print(a,b)
# using 3rd variable
c=a
a=b
b=c
print(a,b)

'''
#----------
'''
a="V"
b="S"
print(a,b)
a,b=b,a
print(a,b)
'''
#--------------
'''
a=10
b=20
print(a,b)
a,b=b,a
print(a,b)
#----------
a=10
b=20
print(a,b)
a=a+b # a= 30
b=a-b # b=30-20 = 10
a=a-b # a=30-10 = 20
print(a,b)

'''
#-----------------
'''
# fibonacci series
# 0 1 1 2 3 5 8 13 21......
n=int(input("Enter number of numbers of fibonacci series : "))
a=0
b=1
if n<0:
    print("Fibonacci series for -ve number is not defined")
elif n==0:
    print("No fibonacci series")
elif n==1:
    print(a)
elif n==2:
    print(a," ",b)
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        
'''
#--------------------
'''
#any 5 functions of list.
#any 5 functions of sets and dictionary
l=[]
for i in range(0,5):
    x=int(input("Enter any number : "))
    l.append(x)
print(l)
for i in l:
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
'''
#-----------------------------------
# code for armstrong number
'''
n=input("Enter number : ")
m=len(n)
s=0
for i in range(m):
    s+=int(n[i])**m
if s==int(n):
    print("Armstrong number")
else:
    print("not")
'''
#-----------
'''
n=input("Enter number : ")
m=len(n)
print(m)
print(n[0],n[1],n[2],n[3])
print(int(n[0])**m)
'''
#--------------
'''
n=int(input("Enter number : ")) #153 , 154
temp=n
s=0
while temp>0:
    digit=temp%10
    s+=digit**3
    temp//=10
if s==n:
    print("Yes")
else:
    print("No")
'''
#---------------
'''
n=153
temp=153
s=0
153>0-  yes
digit = 153%10 = 3
s=s+digit**3 => 0+3**3 = 27
temp=temp//10 =>153//10 =>15

2nd loop - temp - 15>0 -yes
digit = 15%10 = 5
s=s*digit**3 => 27+5**3 =>27+125 = 152
temp=temp//10 = 15//10 = 1

3rd loop  - temp - 1>0 - yes
digit=1%10 = 1
s=s+digit**3 =>152+1**3 = 152+1=153
temp=1//10 = 0

4th loop - temp>0 no

s==n? = 153==153 : yes = yes

'''
#------

# take 5 numbers input from user
# put in a list and then check if prime or not.
'''
k=[int(input("Enter a number : ")) for i in range(5)]
print(k)
p=[]
for j in k:
    if j<0 or j==0:
        print(f"{j} not prime")
    else:
        for i in range(2,j):
            if j%i==0:
                print(f"{j} not prime")
                break
        else:
            print(f"{j} is prime")
            p.append(j)
print(f"Prime numbers list : {p}")
'''
#--------------------
'''
def f(x):
    return x*x
a=f(5)
print(a)

f=lambda x:x*x
a=f(5)
print(a)

u=list(range(1,10))
a=list(map(lambda x:x*x,u))
print(a)

u=list(range(1,10))
a=list(filter(lambda x:x%2==0,u))
print(a)

f=[1,2,3]
g=["Apple","Banana","Cherry"]
h=list(zip(f,g))
print(h)
h=dict(zip(f,g))
print(h)

#reduce
from functools import reduce
k=list(range(2,6))
print(k)
result= reduce(lambda x,y:x*y,k)
print(result)
'''

#----------
#Factors of a number:
num= int(input("Enter a number:"))
a=[]
if num<0 or num==0:
    print(f"1")
else:
    for i in range(1,num+1):
        if num%i==0:
            a.append(i)
print(a)











                                


