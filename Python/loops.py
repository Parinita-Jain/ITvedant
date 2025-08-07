'''
i=1
print(i,end="\n")
i+=1 # i=i+1
print(i,end=" ")
i+=1
print(i,end=" ; ")
i+=1
print(i,end=" * ")
'''
#------------------
'''
print(range(1,5))
for i in range(1,5):
    print(i)
'''
#--------------------
'''
# use range -- range(7,141,7)
for i in range(1,21):
    print(f"7 * {i} = {7*i}")
'''
#-----------------------
'''
for i in range(10,0,-1):
    print(i,end=" ")

'''
#----------------
'''
for i in range(10,0,-2):
    print(i,end=" ")
'''
#------------------
'''
for i in range(10,0,-1):
    if i%2!=0:
        print(f"{i} is odd")
    else:
        print(f"{i} is even")
    
'''

#----------------
'''
m=1
for i in range(1,6):
    m=m*i
print("Factorial of numbers 1 to 5 : ",m)

'''
#--------------------
'''
i=1
while i<=10:
    print(i)
    i=i+1
'''
#--------------
'''
i=10
while i>0:
    print(i)
    i=i-1
'''
#---------------
# 1*2*3*4*5=120
# iterate on numbers starting from 1 till 5. so, iterator is i
# increase value of i by 1
# multiply previous value m with current value of i =m*i
# assign above calculation where in m only
'''
m=1
i=1
while i<=5:
    m=m*i
    i=i+1
print(m)

'''
#---------------
'''
# 5*4*3*2*1=120
# m=1, i=5 i>=1, i=i-1
# m=m*i
m=1
i=5
while i>=1:
    m=m*i
    i=i-1
    print(m)
'''
#-----------------------
'''
#break
for i in range(1,11):
   if i%7==0: #
       print("Inside If")
       break
   print("Inside For")
   print(i)
print("Outside For")

'''
#------------------------
'''
i=7
while True:
    v=int(input("Guess the number between 1 to 10 : "))
    if v==i:
        print("U guessed the number right")
        break
print("Outside while")
'''
#-----------------------------
'''
#continue
for i in range(1,11):
   if i%7==0: #
       print("Inside If")
       continue
       print(i)
   print("Inside For")
   print(i)
print("Outside For")

'''
#--------------------
'''
for i in range(1,5):
    pass
    
'''
#--------------------
'''
ch=int(input("Enter 1 for factorial calculation, 2 for exit"))
if ch==1:
    # factorial loop
    m=1
    i=1
    while i<=5:
        m=m*i
        i=i+1
    print(m)
elif ch==2:
    print("Bye")
    #break
else:
    print("Invalid choice")

'''
#-------
'''
for i in range(1,5):
    for j in range(5,9):
        print(f"{i} value {j} value")

'''
#-------------
'''
for i in range(1,5):
    for j in range(1,4):
        print(j,end="")
    print()
'''
#----------------------
'''
for i in range(1,5):
    for j in range(1,4):
        print(i,end="")
    print()

'''
#-----------
'''
print("a"*5)
for i in range(1,6):
    print("*"*5)

'''
#------------------
'''
for i in range(1,5):
    print("*"*i)
'''
#--------------------
n=17
for i in range(2,n):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Yes ! A prime number")
print("Outside for ")





























