# calculate simple interest
# si=(p*r*t)/100
# assume values for p,r,t
p=int(input("Enter principal amount : "))
print(type(p))
r=int(input("Enter rate amount : "))
t=int(input("Enter time : "))
si=(p*r*t)/100 # (100*7*2)/100=14
print(f"""The simple interest for \nprincipal : {p},
rate : {r}, \ntime : {t} is : \n{int(si)}""")


