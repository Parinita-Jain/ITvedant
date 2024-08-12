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



















        

        
