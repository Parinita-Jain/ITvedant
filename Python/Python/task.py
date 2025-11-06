'''
n=[23,22,29,39,3,2,7,6]#int(input("Enter a number"))
l=[]
for i in n:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        #print(i)
        l.append(i)
print(l)
'''
#----------
'''
a=10
b=20
print(f"Before swapping : {a} and {b}")
temp=a
a=b
b=temp
print(f"After swapping : {a} and {b}")
'''
#------------------------------
'''
a=10
b=20
print(f"Before swapping : {a} and {b}")
a,b=b,a # tuple unpacking
print(f"After swapping : {a} and {b}")
'''
#--------------------------------
'''
#Fibonacci Series
n=8
a=0
b=1
print(f"{a} {b}",end=" ")
for i in range(2,n+1):
    s=a+b
    print(f"{s}",end=" ")
    a=b
    b=s
'''
#---------------------------------
'''
n=8
a=0
b=1
print(f"{a} {b}",end=" ")
i=2
while i<=n:
    s=a+b
    print(f"{s}",end=" ")
    a=b
    b=s
    i=i+1
'''
#-------------------------------
'''
n=int(input("Enter a number : "))
m=str(n)
s=0
for i in m:
    #print(i)
    s=s+int(i)**3
if s==n:
    print("Armstrong number")
else:
    print("Not an armstrong number")
'''
#--------------------------------
'''
n=input("Enter a number : ")
print("Number of digits are : ",len(n))
'''
#-------------------------------
'''
data=[25,None,'NA',45,'',12,'N/A','na',78]
cleaned_data=[]
for i in data:
    if i not in(None,'NA','','N/A','na'):
        cleaned_data.append(i)
print(cleaned_data)
'''
#----------------------------------
'''
data=[10,20,30,40,50,60]
avg_data=[]
for i in range(len(data)-2):
    s=(data[i]+data[i+1]+data[i+2])/3 # sum(data[i:i+3])/3
    avg_data.append(s)
print(avg_data)  

'''
#----------------
'''
data=[('Monday',32),('Tuesday',35),
      ('Wednesday',35),('Thursday',30)]

highest_temp=data[0][1]

for day,temp in data:
    if temp>highest_temp:
        highest_temp=temp

hottest_days=[]
for day,temp in data:
    if temp==highest_temp:
        hottest_days.append((day,highest_temp))

print("Hottest days : ",hottest_days)
'''
#---------------------
'''
# list of user_ids representing each purchase
pur=[101,102,103,101,104,105,102,106,101]
user_counts={}
for i in pur:
    if i in user_counts:
        user_counts[i]+=1
    else:
        user_counts[i]=1
repeat_buyers=[]
for k,v in user_counts.items():
    if v>1:
        repeat_buyers.append(k)
print(repeat_buyers)
print("Number of repeat_buyers are : ",len(repeat_buyers))
'''
#-------------------
'''
t=(1,2,1,2,1,2,1,2,3)
print(t)
print(type(t))
l=list(t)
print(l)
print(type(l))
l.extend([6,2,3,80,90])
print(l)
t=tuple(l)
print(t)
print(type(t))
s=set(t)
print(s)
print(type(s))
t=tuple(s)
print(t)
print(type(t))
'''
#---------------------------------------
'''
l=[10,20,10,30,40,10,20]
d={}
print(l)
for i in l:
    if i in d:
        d[i]=d[i]+1
        print("If mode : increasing previous value and assigning", d)
    else:
        d[i]=1
        print("Else mode : new key created",d)
print(d)

'''
#------------
'''
data=[50,100,150,200]
total=sum(data)
s=0
for i in data:
     s=s+i
per_contri=[(i/total)*100 for i in data]
for i in range(len(data)):
    print(f"{data[i]} and its percentage contribution : {per_contri[i]}")

'''
#-------------------
'''
s="This sentence is composed of some long words and short words"
m=s.split()
print(m)
l=[i for i in m if len(i)>5 ]
print("Total number of words greater than 5 are : ",len(l))
print(f"{l}")
'''
#---------------------
'''
emails=["alice@gmail.com","bob@yahoo.com","charlie@outlook.com"]
domains=[]
for i in emails:
    domain=i.split("@")
     #print(domain)
    #print(domain[1])
    domains.append(domain[1])
print(domains)
'''
#----------------------------
'''
data=[10,40,30,20,40]
u_d=list(set(data))
print(u_d)
u_d.sort(reverse=True)
print(u_d)
if len(u_d)<2:
    print("No second highest element")
else:
    print(u_d[1])
'''
#------------------------
'''
s=set(range(1,6))
print(s)
e=3
s.discard(e)
print(s)
'''
#-------------------------------------
'''
data={'a':10,'b':50,'c':40}
#give the key with the highest value
print(data.get('a'))
max_key=max(data,key=data.get)
max_value=max(data.values())
print(max_key)
print(max_value)
'''
#------------------------
'''
s1={1,2}
s2={2,3,4,5}
print(s1.issubset(s2))
'''
#-----------------------
'''
try:
    n=int(input("Enter a number : "))
    print(n**2)
except ValueError as e:
    print("Enter valid whole number.")
else:
    print("Successful Completion ")
finally:
    print("Executed")

'''
#-----------------------------
'''
class product:
    def __init__(self,pro_id,n,pr,q):
        self.product_id=pro_id
        self.name=n
        self.price=pr
        self.quantity=q
    def details(self):
        return f"{self.name},{self.price},{self.quantity}"
    def display(self):
        print(f"{self.product_id}{self.name}{self.price} {self.quantity}")
        
obj1=product(1,"Mobile",19000,2)
obj1.display()
print(obj1.details())
'''
#---------------------
line_count=0
word_count=0
with open("test1.txt",'r') as f:
    r=f.readline()
    while r:
        line_count=line_count+1
        print(f"{r} {r.split()} {len(r.split())}")
        word_count=word_count+len(r.split())
        print(f"word_count : {word_count}")
        r=f.readline()
        
print("Total lines : ",line_count)
print("Total words : ",word_count)
    













