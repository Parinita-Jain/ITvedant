'''
f=open("test.txt") # file handler
print(f)
print(type(f))
print(f.tell()) # tell() tells the position of cursor
print(f.read())
print(f.tell())
f.seek(4) # reposition cursor with seek
print(f.tell()) # tell() tells the position of cursor
print(f.read())
print(f.tell()) 
'''
#------------------
'''
f=open("test.txt","r")
# readline()
r=f.readline() # read characters from very start of line to \n
while r: # while r!=EOF
    print(r,"-----------")
    r=f.readline()
print(f.tell())
f.seek(0)
print(f.readlines())
f.seek(0)
#f.write("yuppok")
#f.close()
'''
#----------------------------
'''
f=open("test.txt","w")
f.write("Hi ! This is write mode.")
f.close()
'''
#-------------------
'''
with open("test1.txt","w") as f:
    f.write("Hi ! This is write mode with with.")
    
'''
#------------------------
'''   
with open("test3.txt","a+") as f:#a+:a+r.Cursor at the end and then write
    f.write("Hi ! This is append mode with with.")
    print(f.tell())
    f.seek(0)
    print(f.read())
'''
#-------------------------------
'''  
with open("test3.txt","r+") as f: # r+:r+a, Cursor at the start and then write
    f.write("Hi Again ! This is r+ mode with with.")
    print(f.tell())
    f.seek(0)
    print(f.read())

'''
#-------------------------
'''
#d=[10,20,10,30,40,50]
d=str(40)
print(type(d))
with open("test3.txt","wt+") as f: # t= text
    f.write(d)
    f.seek(0)
    print(f.read())

'''
#=================
# b - binary
import pickle
d=[10,20,10,30,40,50]
with open("test.txt","wb+") as f: # open file in b-binary mode
    # pickling/serialization
    se=pickle.dumps(d)
    print("Serialization",se)
    print(type(se))
    f.write(se)
    #unpickling/deserialization
    f.seek(0)
    r=f.read()
    print("r",r)
    print("r",type(r))
    m=pickle.loads(r)
    print("deseralized",m)
    print(type(m))





    
    
        
f














