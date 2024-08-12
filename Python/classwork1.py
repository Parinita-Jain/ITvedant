'''
l=int(input("Enter length : "))
b=int(input("Enter breadth : "))
print("Area of rectangle is : ",l*b)

'''
#--------------
'''
r=int(input("Enter radius : "))
print("Area of circle is : ",3.14*(r**2)) #3.14*r*r
'''
#-------
'''
l=int(input("Enter length : "))
b=int(input("Enter breadth : "))
c=l
l=b
b=c
print(f"The swapped values are : {l} , {b}")

'''
#--------------
'''
n=int(input("Enter number : "))
if(n%2==0):
    print("Number is even")
else:
    print("Number is odd")
'''
#--------------

n=int(input("Enter number : "))
if((n%3==3)and(n%5==0)):
    print("Number divisible by both 3 and 5")
elif((n%3==0)and(n%5!=0)):
    print("Number divisible by 3 and not by 5")
elif((n%5==0)and(n%3!=0)):
    print("Number divisible not by 3 and only by 5")
else:
    print("Number not divisible by both 3 and 5")
print("The end of prog")    









    

