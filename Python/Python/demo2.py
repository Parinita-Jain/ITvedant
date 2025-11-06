'''
# Float datatype
a=2.3
b=4.6
print(a**b) # 2.3 raise to power 4.6 -- float result
print(a%b) # float only remainder
print(a//b) # float value
'''
#--------------- string datatype
'''
a="Hello"
b="World"
print(type(a))
print(a+b) # concatenation
#print(a-b) # error
#print(a*b) # error
print(a*5)
#print(a/5) #error
'''
#------------------- logical operators
# and or not
# ------------------ relational operator
# > ,<, >=,<=, ==, !=
'''
a=20
b=30
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a<b)
print(a>b)
'''
#-----------------------------
'''
profit=float(input("Enter profit value : "))
if profit<0:
    print("Inside If. Part of if")
    print("Alert : Profit less than 0")
print("Outside if. Not part of if")
'''
#-------------------
'''
profit=float(input("Enter profit value : "))
if profit<0:
    print("Inside If. Part of if")
    print("Alert : Profit less than 0")
elif profit==0:
    print("Inside elif")
    print("Attention : Profit is 0")    
else:
    print("Inside else.")
    print("Great ! Profit is +ve")
print("Common statement")
'''
#----------------------------------
'''
n=int(input("Enter a value : "))
if n%2==0:
    print("Even")
else:
    print("Odd")

'''
#--------------
'''
m=int(input("Enter a value : "))
if m>=75 and m<=100:
    print("Grade A")
elif m>=60 and m<=74:
    print("Grade B")
elif m>=35 and m<=59:
    print("Grade C")
elif m>=0 and m<=34:
    print("Fail")
else:
    print("Enter valid marks")
'''
#---------------------
a=input("Enter any alphabet : ")
if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
    print("Vowel")
else:
    print("Consonant")







   













