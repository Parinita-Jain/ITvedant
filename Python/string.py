'''
for i in range(5):
    print(i)
    if i==3:
        print("Inside if")
        break
else:
    print("Loop completed")
print("Outside loop")
'''
#-----------------------------
'''
# String
a="Hello World !"
print(a)
print(type(a))
print(a[0]) # indexing -- value at the given index
print(a[-1])
print(len(a))
print(a[-len(a)])
print(a[len(a)-3])
'''
#--------------
'''
# Slicing -- chunk or many values 
# String
a="Hello World !"
print(a[:7])
print(a[:len(a)])
print(a[-5:-1])
print(a[::2])
print(a[::])
print(a[::-1])
'''
#-------------------
#String Functions--
a="Hello World !"
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.count('l'))
print(a.startswith("h"))
print(a.endswith("!"))
print(a.find('d'))
print(a.index('d'))
print(a.isnumeric())
print(a.isalpha())
print(a.isalnum())
print(a.replace("Hello","Hi"))
print("z" in a)
print("z" not in a)

a="153_rer"
print(a.isnumeric())
print(a.isalpha())
print(a.isalnum())






































