'''
marks=float(input("Enter marks  : "))
if (marks>=75) and (marks<=100):
    print("Grade A")
elif (marks>=60) and (marks<=74):
    print("Grade B")
    print("Practice More")
elif (marks>=35) and (marks<=59):
    print("Grade C")
else:
    print("F")
print("Completely outside conditional statement")

'''
#-------------------------------------------------------------------------------------------------
'''
i=1
a=2
print(f"{a}*{i}={a*i}")
i=i+1
print(f"{a}*{i}={a*i}")
i=i+1
print(f"{a}*{i}={a*i}")
i=i+1
print(f"{a}*{i}={a*i}")
i=i+1
print(f"{a}*{i}={a*i}")

'''
#-----------------------------
'''
a=2
for i in range(1,6):
    print(f"{a}*{i}={a*i}")

'''
#--------------
'''
for i in range(0,51):
    if i%2==0:
        print(i,end=",")
'''
#-----------------
'''
for i in range(0,51,2):
        print(i,end=",")
'''
#--------------------------------------------------------
'''
for i in range(51,100,2):
        print(i,end=",")
print()
print()
#----------------
for i in range(50,-1,-2):
        print(i,end=",")
print()
print()
#-------------
for i in range(99,50,-2):
        print(i,end=",")
print()
print()
#-----------------
'''
#----------------
'''
for i in range(0,51):
    if i%2==1:
        print(f"{i} is odd")
    else:
        print(f"{i} is even")
else:
    print("Hi ! Else part of For")
print("Completely outside loop")
'''
#------------------------------------------------
'''
for i in range(2,51):
    if i%29==1:
        print(f"The number is {i}")
        break
    else:
        print(i,end=",")
else:
    print("Hi ! Else part of For")
print("Completely outside loop")
'''
#--------
'''
for i in range(2,51):
    if i%29==1:
        print(f"Good !")
        continue
        print("Hello World !")
    else:
        print(i,end=",")
else:
    print("Hi ! Else part of For")
print("Completely outside loop")
'''
#-----------------------
for i in range(2,51):
    if i%29==1:
        pass
    else:
        print(i,end=",")
else:
    print("Hi ! Else part of For")
print("Completely outside loop")











