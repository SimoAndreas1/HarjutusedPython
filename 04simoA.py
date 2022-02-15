#Ülesanne 4
#10.02.2022
#Simo Andreas Novikov

#Ruut
'''
a = int(input("1.külg: "))
b = int(input("2.külg: "))

if a==b:
    print("see on ruut")
else:
    print("see on ristkülik")
'''    
'''    
#Matemaatika

arv1 = int(input("Sisesta üks arv: "))
arv2 = int(input("Sisesta teine arv: "))
tehe = input("vali tehe + - * / ")
if tehe == "+":
    vastus = arv1 + arv2 
if tehe== "-":
    vastus = arv1 - arv2

if tehe== "*":
    vastus = arv1 * arv2

if tehe== "/":
    vastus = arv1 / arv2

print(f"{arv1}{tehe}{arv2}={vastus}")
'''
'''
#juubel
sünnipäev = input("ütle oma sünnipäev kujul dd.mm.yyyy: ")
dd, mm, yyyy = sünnipäev.split(".")
praegu = 2022
vanus = praegu-int(yyyy)
jaanus = vanus%5
if jaanus==0:
    print("juubel")
else:
    print("ei ole juubelit")
'''


'''
#Müük
hind = int(input("Sisesta toote hind: "))
if hind<10:
    ale = 0.1
else:
    ale = 0.2
vastus = hind-(hind*ale)
print(vastus)
'''

'''
#Jalgpalli Meeskond

sugu = input("sisesta oma sugu: ")

if sugu=="mees":
    vanus = int(input("sisesta oma vanus: "))
    if vanus >= 16 and vanus <=18:
        print("sobid meeskonda")
    else:
        print("ei ole sobilik")
        
else:
    ()
'''


#tärnid
'''
for e in range(1,6):
    for a in range(1,6):
        print("* ",end="")
    print()
print ("-"*10)

for e in range(1,6):
    print(e*"* ")
print ("-"*10)
k = 6
for e in range(1,6):
    print(k*"* ")
    k = k -1
'''

'''
#Loto

import random

for e in range(1,6):
    a = int(random.randint(0,9))
    print(a,end="")
'''


#Paaris ja paaritu
'''
for a in range(1,101):
    
    jaak = a%int(2)
    
    if jaak == 0:
        print(a,"paarisarv")
    else:
        print(a,"paaritu arv")
'''

#pisike korrutustabel
'''        
for i in range(1,11):
    print(f"5 x {i} = {i*5}")
'''


#Viisikud
'''
for i in range(1,101):
    jaak = i%int(5)
    if jaak == 0:
        print(i)
    else:
        ()
'''

#arvamismäng

import random

loop = 1
korrad = 1
suv = random.randint(1,10)
while loop == 1:
    if korrad <= 3:
        arv = int(input("arva ära arv 1-10: "))
        else:
            veel = input("tahad veel mängida? jah või ei: ")
            if veel =="jah":
                korrad = 0
            else:
                loop = 0
            korrad += 1
            if arv == suv:
                print("õige vastus")
            else:
                print("ei arvanud ära")
            print(suv, arv)
        print("mäng läbi")
