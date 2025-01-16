'''
a=10
b=0
print(a/b)

a=[1,2,3,4,5]
print(a[5])
'''
try:
    a=10
    b=0
    #print(a/b)
    a=[1,2,3,4,5]
    #print(a[5])
    d={1:1,2:4,3:9}
    print(d[2])
except ZeroDivisionError as e:
    print("Dividing by zero is not allowed")
except IndexError as e:
    print("Accessed index out of range")
except(KeyError,ValueError) as e:
    print("Key or value error")
except Exception as e:
    print("Common error",e)
else:
    print("Else statement is executed in case of no raised exception")
finally:
    print("Finally statement is executed in any case")
    



    
