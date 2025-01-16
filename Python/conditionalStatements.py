'''
# Relational Operators -- they compare 2 values and return a boolean(True/False)
# ==,!=,>,<,>=,<=
a=10
b=20
# check if a's value is equal to b's value
print(a==b) # relational operator
print(a>=b)
print(a<=b)
print(a!=b)
'''
#------------------------
'''
#Logical operator -- combines multiple conditions and give boolean output.
# and, or , not
a=14
print(a>10 and a<20)
n="Alic"
print(n=="Alice" or a>100)
b=23
print(not(n=="Alice" or a>100))
'''
#--------
# Conditional stmts -- if, if-else, if-elif-else
'''
n=input("Enter name : ")
if "u" in n:
    print(f"Hello ! {n}")
    print("Inside if")
elif "a" in n:
    print("a is present")
elif "e" in n:
    print("e is present")
elif "i" in n:
    print("i is present")
elif "o" in n:
    print("o is present")
else:
    print("Vowels not present")
print("Outside if ")
'''
#-----------------------
'''
n=input("Enter letter : ")
if "a" in n or "e" in n or "i" in n or "o" in  n or "u" in n:
    print("U entered a Vowel")
else:
    print("It's  consonant")
'''
#--------------
'''
n=input("Enter letter : ")
if "a"==n or "e"==n or "i"==n or "o"==n or "u"==n:
    print("U entered a Vowel")
else:
    print("It's  consonant")

#in,not in are membership operator
'''
#-------------------
'''
n=input("Enter letter : ")
if n in ("a","e","i","o","u"):
    print("U entered a Vowel")
else:
    print("It's  consonant")

'''
#----------------------
'''
n=int(input("Enter marks : "))
if n>=75 and n<=100:
    print("A")
elif n>=60 and n<=74:
    print("B")
elif n>=35 and n<=59:
    print("C")
else:
    print("F")

'''
'''
n=int(input("Enter marks : "))
if n%2==0:
    print("Even")
else:
    print("Odd")
'''
#--------------

ch=int(input('''
Enter choice:
    1.Simple Interest Calculation
    2.Area of triangle calculation : '''))
if (ch==1):
    p,r,t=1000,2,2
    print("SI ",(p*r*t)/100)
elif(ch==2):
    b,h=100,50
    print("Area ",(0.5*b*h))
else:
    print("Please enter valid choice ")











    











