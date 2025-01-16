'''
f=open("test.txt")
print(f.tell())
print(f.read()) # read() -- read complete file till the end in 1 go 
print(f.tell())
f.seek(4)
print(f.tell())
print(f.read())
print(f.tell())
'''
#----------
# readline()
'''
f=open("test.txt","w")
t=f.readline()
while t:
    print(t,end="")
    t=f.readline()
print(f.tell())
f.seek(0)
print(f.readlines())
f.seek(0)
f.write("yytuyuy")
f.close()

'''
#-------------------
'''
f=open("test.txt","w")
f.write("yytuyuy hkr jfghfugh grjgh gjfh jhgdjfgh")
f.close()
'''
#---------
'''
with open("test.txt","w") as f:
    f.write("yytuyuy hkr jfghffyt78")
'''
#---------
'''
with open("test.txt","a") as f:
    f.write("\nHello , I am in append mode")

'''
#------------
'''
# a+ -- cusor at end and then appended
f=open("test.txt","a+")
f.write(" tfygrejhg gryfu")
f.seek(0)
print(f.read())
'''
#-------------
'''
#-- r+ -- cursor is positioned at the beginning and appended
f=open("test.txt","r+")
f.write(" gygyu guhi")
f.seek(0)
print(f.read())
'''
#------------
'''
# w+ -- overwrite and write from the 0th index
f=open("test.txt","w+")
f.write(" 6567 gygyu guhi")
f.seek(0)
print(f.read())
'''
#----
'''
f=open("def.txt","wt")
'''
#---------------
#-- serialization and deserialization
import pickle
#l=[1,2,3,4,5]
l={"abc":[1,2],"def":[3,4]}
with open("def.txt","wb+") as f: # b - binary mode , t- text mode
    # pickling / serialization
    se=pickle.dumps(l)
    print(se)
    print(type(se))
    f.write(se)
    # unpickling/deserialization
    f.seek(0)
    r=f.read()
    m=pickle.loads(r)
    print(m)
    print(type(m))





















































