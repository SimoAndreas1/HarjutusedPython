# Ülesanne 07
# Simo Andreas Novikov
# 17.02.2022

'''
def tervita(n,k="de"):
    if k == "et":
        print("tere",n)
    elif k == "en":
        print("hi",n)
    else:
        print("hallo",n)
    
tervita("mario","et")
'''



import math

def kuup(n):
    v = n ** 3
    return v

def kera(r):
    v = 4/3*3.14*r**3
    return v

def koonus(r, h):
    v = 1/3*3.14*r**2,h
    return v

def Silinder(r, h):
    v = 3.14*r**2,h
    return v

print("********** LEIAME RUUMALA **********")
print("vali kujund:\n1 kuup\n2 kera\n3 koonus\n4 silinder")
valik = int(input("Vali kujund: "))
if valik == 1:
    k=int(input("Sisesta kuubi üks külg: "))
    print("kuubi ruumala on",(k))

elif valik == 2:
     r=int(input("Sisesta kera raadius r= "))
     print("kera ruumala on",(r))
     
elif valik == 3:
     h=int(input("Sisesta koonuse raadius r= "))
     print("Koonuse ruumala on",(h))
     
elif valik == 4:
     h=int(input("Sisesta Silindri raadius r= "))
     print("Silindri ruumala on",(h))
     
    
