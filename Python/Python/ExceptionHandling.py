'''
a=10
b=0
c=a/b #---error
print(c)
'''
#------------
'''
try:
    a=int(input("Enter a number : "))
    b=int(input("Enter another number : "))
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("Denominator cannot be zero")
else:
    print("Else is executed in case of no exception")
finally:
    print("Finally is executed regardless of exception is raised or not")
    b=1
    c=a/b
    print(c)
'''
#-------------------
'''
l=[1,34,56,32,7]
print(l[7])
d={1:1,2:4}
d[4]
'''
#-------------
'''
try:
    l=[1,34,56,32,7]
    print(l[3])
    d={1:1,2:4}
    print(d[2])
    a=l/"b"
except IndexError as e:
    print(e)
except KeyError as e:
    print(f"key {e} doesnot exist in dictionary")
except Exception as e:
    print("Common error")
'''
#---------------------
    








    
