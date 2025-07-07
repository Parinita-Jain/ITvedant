'''
for a in range(1,6):
    print(' '*(5-a),end='')
    print('* '*a)
'''
#---------------
'''
for a in range(1,6):
    print(' '*(5-a),end='')
    print('*'*a)
'''
#-------------------
'''
for i in range(1,6): #1,2,3,4,5
    for j in range(1,i+1):
        print(i,end='')
    print()
'''
#-----------------------
'''
for i in range(1,6): #1,2,3,4,5
    for j in range(1,i+1):
        print(j,end='')
    print()
'''
#-----------------------
'''
row=int(input('Enter the number of row you want? '))

for i in range(1,row+1): 
    for j in range(1,i+1):
        print('*',end='')
    print()
'''
#-------------
'''
row=int(input('Enter the number of row you want? '))
val=65 #65 is the ASCII value for A, 66 is ASCII value for B
for i in range(1,row+1): 
    for j in range(1,i+1):
        print(chr(val),end='')
    val+=1
    print()
    '''
#-----------------------------
'''
7.
num = int(input("Enter a number: "))
original = num
n = len(str(num))
sum_of_powers = 0

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** n
    num //= 10

if sum_of_powers == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")
8.
num = int(input("Enter a number: "))
original = num
digits = str(num)
n = len(digits)
sum_of_powers = 0

for digit in digits:
    sum_of_powers += int(digit) ** n

if sum_of_powers == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")
9.
num = int(input('Enter a number ')) #11

for i in range(2,num): #(2,19) ==> 2,3,4,5,6,7,8,9,10
    if num%i==0:
         print(num,'It is not.')
         break
else:
    print(num,'It is')
10.
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)
11.
n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)
12.
for i in range(1, n):
    print(' ' * (n - i) + '* ' * i)
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)
    '''
#-------------------------------------
'''
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()
'''
#---------------------------------------
'''
for num in range(100, 301):
    if num > 1:
        is_prime = True  
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                is_prime = False  
                break  
        if is_prime:
            print(num)
'''
