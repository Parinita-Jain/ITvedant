'''
a=int(input("Enter a number : "))
print(f"The number {a} after dividing by 2 : {a//2}")
print(type(a))
'''
#------------------------
'''
# Addition of 2 numbers

n1=float(input("Enter number : "))
n2=float(input("Enter another number : "))
#s=n1+n2
print(f"The addition of numbers is : {n1+n2}")
'''
#---------------
'''
# ci calculation
p=float(input("Enter principal : "))
r=float(input("Enter rate : "))
t=float(input("Enter time : "))

ci= p*(1+(r/100))**t
print(f"The ci of {p},{r} and {t}: {ci}")
'''
#----------------------
'''
# + - * / // ** => numbers
# conditional operators which helps in checking whether
# a condition is satisfied or not. => true/false
# >,<,==,<=,>=
a=12
b=15
print(f"{a} > {b} : {a>b}")
print(f"{a} < {b} : {a<b}")
print(f"{a} == {b} : {a==b}")
'''
#-------------------------
'''
#to- check if number is even or odd
a=int(input("Enter a number : "))
if (a%2==0) and (a>70):
    print(f"{a} is an even number and > 70")
elif (a%2==1) and (a>70):
    print(f"{a} is an odd number and > 70")
elif (a%2==1) and (a<=70):
    print(f"{a} is an odd number and <= 70")
else:
    print(f"{a} is an even number and <= 70")
'''
#-----------------------
'''
v=input("Enter letter : ")
if v=="a" or v=="e" or v=="i" or v=="o" or v=="u":
    print("Vowel")
else:
    print("consonant")
    
'''
#--------------------
v=input("Enter letter : ")
if v in ("a","e","i","o","u"):
    print("Vowel")
else:
    print("consonant")













