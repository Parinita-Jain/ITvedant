'''
c=input("Enter country Name : ")
if c in ("India","Finland","Iceland","Sweden"):
    print("Great choice")
else:
    print("Guess another")
'''
#--------------------------
'''
for i in range(5): # 1,6--- 6-
    c=input("Enter country Name : ")
    if c in ("India","Finland","Iceland","Sweden"):
        print("Great choice")
        break
    else:
        print("Guess another")
'''
#--------------
'''

ch=input("""Do u want to play
            Guess the country game ? Enter Y/N : """)
while ch in ("Y","y","yes","Yes","YES"):
    c=input("Enter country Name : ")
    if c in ("India","Finland","Iceland","Sweden"):
        print("Great choice")
        ch=input(""" IF --> Do u want to play
            Guess the country game ? Enter Y/N : """)
        if ch in ("N","n","no","No"):
            break
    else:
        ch=input("""Do u want to play
            Guess the country game ? Enter Y/N : """)
print("Happy Times ! Play again")
        
'''
#-------------
# 1 to 10
'''
i=1
while i<11:
    print(i,end=" ")
    i=i+1
'''
#---------
'''
i=51
while i<=51 and i>=25:
    if i%2==1:
        print(i,end=" ")
    i=i-2
 
'''
#----------------
'''
i=51
while i>=25:
    print(i,end=" ")
    i=i-2
'''
#-------------------
'''
s=0
for i in range(1,8):
    print(f"Before addition : s:{s} + i:{i} = ",end=" ")
    s=s+i
    print(f"{s}")

'''
#------------------
'''
s=1
for i in range(1,8):
    print(f"Before Multiplication : s:{s} * i:{i} = ",end=" ")
    s=s*i
    print(f"{s}")
'''
#------------------
s=0
for i in range(1,8):
    s=s+i
print(f"{s}")






