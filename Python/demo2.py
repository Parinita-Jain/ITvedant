'''
a=10
b=5
total=a+b
print("First number : ",a)
print("Second number : ",b)
print("The total of the numbers is : ",total)
------------------------------------------
'''

#-----------------
'''
a=int(input("Enter first number : ")) # float()
b=int(input("Enter second number : "))
total=a+b
print("First number : ",a)
print("Second number : ",b)
print("The total of the numbers is : ",total)
print(type(a),type(b))
'''

#--------------------
'''
a=int(input("Enter first number : ")) # float() a=6
b=int(input("Enter second number : ")) # b=6
c=a==b
print("c : ",c)
if(c):
    print("Are the number entered equal : Yes")
else:
    print("Are the number entered equal : No")
'''
#--------------------
a=int(input("Enter first number : ")) # float() a=6
b=int(input("Enter second number : ")) # b=6

if(a>b):
    print("The first number is greater")
elif(a==b):
    print("The numbers are equal")
elif(a<0):
    print("First number is negative")
else:
    print("The second number is greater")

    

