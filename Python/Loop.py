'''
print(f"2 * 1 = ",2*1)
print(f"2 * 2 = ",2*2)
print(f"2 * 3 = ",2*3)
print(f"2 * 4 = ",2*4)
print(f"2 * 5 = ",2*5)

'''
#--------------------------------
'''
# for loop -- iterations iterating 
for i in range(1,11,2):
    print(f"2 * {i} = {2*i}")
'''
# range()-- syntax -- range(start_index,stop_index,steps)
# by default start index is 0
# step is increment - by 1
# gives values from start_index to stop_index-1
'''
for i in range(1,51,2):
    print(i)
'''
#--------------
'''
for i in range(2,51,2):
    print(i)

'''
#--------------------
#while loop
'''
for i in range(1,6):
    print(i)

'''
'''
i=1
while i<=5:
    print(i)
    i=i+1
'''
'''
i=0
while True:
    a=input("Enter your name : ")
    print(f"Hello {a}")
    ch=input("Do u want to continue :(y/n): ")
    if ch=="n":
        break
print("Outside loop")
'''
'''
for i in range(5):
    if i==3:
        break
    print(f"{i} inside loop")
print("Ouside loop")

'''
'''
for i in range(8):
    if i==3:
        print("Good afternoon")
        continue
        print("Hi")
    print(f"{i} inside loop")
print("Ouside loop")
'''
'''
for i in range(8):
    if i==3:
        print("Good afternoon")
        pass
        print("Hi")
    print(f"{i} inside loop")
print("Ouside loop")

'''
'''
for i in range(8):
    pass
'''
#--------------------------------
'''
for i in range(1,6):
    print(i,end=" ")
'''
#---------------------------
'''
for i in range(1,6):
    print("*"*i)
'''
#-------------
'''
for i in range(5,0,-1):
    print("*"*i)
'''
#----------------
'''
for i in range(1,6):
    if(i==4):
        print("Hello")
    else:
        print(i)
'''
#---------------------
'''
i=2
if(i==2):
    for j in range(5,0,-1):
        print(j)
else:
    print("Good luck")
'''
#-----------------------
# Nested loop
'''
for i in range(1,4):
    for j in range(60,100,10):
        print(f"i:{i} j:{j}")
'''
#-----------
'''
for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")
    print()
'''
#---------------
'''
for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()

'''
1
12
123
1234
#----
1
22
333
4444















































































