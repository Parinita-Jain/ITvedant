'''
# function definition
def func_name(a):
    print(f"Hello {a}")

func_name("Nivedita") # function call
'''
#--------
'''
def addition(a,b,c=0,d=0): # parameters a and b , c and d are Default parameters
    return a+b+c+d
print(addition(2,3,4,5))
c=addition(6,7) # arguments 6 and 7
print(c)
'''
#----------
'''
def addition(*args): 
    print(*args)
    print(args)
    print(type(args))
    print(sum(args))
    return "Hello"

print(addition(1,2,3,4,5))# variable length arguments

'''
#--------------
'''
def b():
    print("B")
def a():
    print("A")
    b()
    print("Back to A")
    return "Returned to the 1st point of call"

c=a() # 1st point of call
print(c)
'''
#-----
'''
# variable scope
x=90 # global scope
def g():
    #print(x,y) #--error
    print(x)
def s():
    y=20 # local scope
    global x
    x=9
    print(x,y)
s()
g()
print(x)
'''
#-------------------
#11 -- 121
'''
def sq(a):
    return a**2
b=int(input("Enter a number : "))
print(sq(b))
'''
#-----
'''
def sq():
    a=int(input("Enter a number : "))
    return a**2
print(sq())
'''
#----
'''
def sq(a):
    return a**2
b=int(input("Enter a number : "))
print(sq(b))
'''
#---
'''
y=lambda a:a**2
print(y(8))

x=lambda a,b:a+b # anonymous function or nameless function or lambda function
c=int(input("Enter a number : "))
print(x(c,3))
'''
#----------------
'''
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
print(addition(2,3))
c=addition(2,4)
print(c)
print(subtraction(2,3))
print(multiplication(2,3))
print(division(2,3))
'''
#--------------
"""
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
while True:
    ch=int(input('''
        Enter Choice :
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit : '''))
    if ch==1:
           print(addition(2,3))
    elif ch==2:
           print(subtraction(2,3))
    elif ch==3:
            print(multiplication(2,3))
    elif ch==4:
            print(division(2,3))
    elif ch==5:
            break
    else:
        print("Enter correct choice")
        
"""      
#----------------
'''
x=lambda a,b:a/b
print(x(6,3))
'''
#-----
'''
x=lambda x:x**2
#l=[1,2,3,4,5]
l=list(range(1,6))
print(list(map(x,l)))
'''
#----------
'''
print(list(map(lambda a:a**2,list(range(1,50)))))
'''
#-------------
#filter()
'''
x=lambda x:x%2!=1
l=list(range(1,51))
print(list(filter(x,l)))
'''
#----------------
'''
def f(n):
    m=1
    for i in range(2,n+1):
        m=m*i
    return m

print(f(5))

'''
#-----
'''
from functools import reduce # built-in module
print(reduce(lambda a,b:a*b,list(range(1,6)))) #[1,2,3,4,5]
'''
#----------------------
# module---

import calculator as c
print(c.addi(2,3))
print(c.subt(6,3))

#----
'''
#from calculator import addi as a,subt as s
from calculator import * # user-defined module
print(addi(2,3))
print(subt(6,3))
'''
#---------
'''
import math
print(math.factorial(5))
print(dir(math))
'''
#---------
# Recursion Function -- The function calling itself
'''
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
print(f(5))

'''
#--------


































    





































