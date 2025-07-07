'''
for i in range(5,26):
    print(i)
'''
#------------------------
'''
for i in ("a","e","i","o","u"):
    print(i)
'''
#--------------------------
# range(starting_criteria,stopping_criteria-1,jump)
'''
for i in range(5,26,5):
    print(i)
'''
#----------------
'''
for i in range(1,21):
    print(f"2 * {i} = {2*i}")
'''
#-----------------------
'''
for i in range(1,7):
    print(i)

'''
#-------------
'''
j=1
while j<=6:
    print(j)
    j=j+1

'''
#-----------------------
'''
# break
for i in range(10,0,-1):
    if i==5:
        print("Inside if")
        break
    print("Inside loop")
    print(i)
print("Outside loop")
'''
#----------------------
#---
'''
i=0
while True:
    n=input("Enter your name : ")
    print(f"Your name is : {n}")
    i=i+1
    ch=input("Do u want this continue (Y/N) : ")
    if ch=="N" or ch=="n":
        break
print(f"U entered names {i} times")

'''
#--------------
'''
# continue
for i in range(10,0,-1):
    if i==5:
        print("Inside if")
        continue
        j=6
        print(j)
        print("After continue")
    print("Inside loop")
    print(i)
print("Outside loop")
'''
#---------------------
'''
# pass
for i in range(10,0,-1):
    pass
'''
#-----------------------
'''
for i in range(10,0,-1):
    print(i,end=" ")
'''
#---------------
'''
for i in range(1,5):
    print(" * "*i)
'''
#------------
'''
for i in range(1,4):
    for j in range(6,10):
        print(f"{i}----------{j}")
'''
#-------------
for i in range(1,7):
    for j in range(1,5):
        print(j,end=" ")
    print()













    



















