#Ülesanne 05
#Simo Andreas Novikov
#15.02.2022

'''
#Nimede lisamine loendisse

nimed = []
for a in range(5):
    nimi = input ("lisa nimi: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)


#Õpilased

opilased = ['Juhan','Kati','Maarja','Mario','Mati']

print("vali number, mida soovid muuta: ")
for a in range (len(opilased)):
    print(f"{a+1}. {opilased[a]}")
valik = int(input("sisestage number: "))
del opilased[valik-1]
u_nimi = input("sisestage uus nimi: ")
opilased.insert(valik-1,u_nimi)
print("nimi uuendatud")
print(opilased)




#Duplikaadid

opilased = ['juhan','Kati','Mario','Mario','Mati','Mati']
puhtad_opilased = []

for i in range(len(opilased)):
    if opilased[i] not in puhtad_opilased:
        puhtad_opilased.append(opilased[i])
        
for i in range (len(puhtad_opilased)):
    print(puhtad_opilased[i],end=", ")



#Vanused

import random
vanused = []
for i in range (5):
    vanused.append(random.randint(1,99))
    
print(vanused)



#tärnid

import random

arvud = []
for a in range(5):
    arvud.append(random.randint(1,99))
print(arvud)
for a in range (len(arvud)):
    print("*"*arvud[a])
'''
