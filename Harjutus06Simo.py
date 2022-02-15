#Ülesanne 06
#Simo Andreas Novikov
#15.02.2022

#Poliitikud

re, kesk, kokku = 0, 0, 0


erakonnad = []
with open ('poliitikud.txt', 'r') as poliitikud:
    for rida in poliitikud:
        enimi, pnimi, erakond, likes = rida.split(" ")
        print(f"{enimi:11} {pnimi:11} {erakond:4} {likes:5}",end="")
        if erakond=="RE":
              re+=1
        elif erakond=="KE":
                      kesk+=1
              
              
print("\n-------------------")
print(f"Reformikad: {re}\nKesikud: {Kesk}\n")
print(f"Erakondi on kokku: {len(erakonnad)}")
print(erakonnad)

