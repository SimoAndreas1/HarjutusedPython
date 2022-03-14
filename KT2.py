#Simo Andreas Novikov
#10.03.2022


import random
correct = 0

while True:
    küsimused = int(input("Lisa mitu küsimust sa soovid vastata: "))
    raskus = input("Lisa küsimuste raskus millele vastata: algaja või raske: ")
math = input ("Vali liitmine või lahutamine: ")

if raskus == "algaja":
    for i in range(küsimused):
        if math == "liitmine":
            alg1 = random.randint(1, 10)
            alg2 = random.randint(1, 10)
            prod = alg1 + alg2
            
            AlgAns = input("Mis on " + str(alg1) + " plus " + str(alg2) + "? ")
            
            if int(AlgAns) == prod:
                print("Vastus on õige -- hästi.\n")
                correct += 1
            else:
                print("Ei, vastus on ",prod)
                
        elif math == "lahutamine":
            alg1 = random.randint(1,10)
            alg2 = random.randint(1,10)
            prod = alg1 - alg2
            
            AlgAns = input("Mis on " + str(alg1) + " miinus " + str(alg2) + "? ")
            
            if int(AlgAns) == prod:
                print("Vastus on õige -- hästi.\n")
                correct += 1
            else:
                print("Ei, vastus on ",prod)
    
elif raskus == "raske":
    for i in range(küsimused):
        if math == "liitmine":
            Ras1 = random.randint(1, 100)
            Ras2 = random.randint(1, 100)
            prod = Ras1 + Ras2
                
            RasAns = input("Mis on " + str(Ras1) + " plus " + str(Ras2) + "? ")
                
            if int(RasAns) == prod:
                print("Vastus on õige -- hästi.\n")
                correct += 1
            else:
                print("Ei, vastus on ",prod)
                    
        elif math == "lahutamine":
            Ras1 = random.randint(1,100)
            Ras2 = random.randint(1,100)
            prod = Ras1 - Ras2
                
            RasAns = input("Mis on " + str(Ras1) + " miinus " +str(Ras2) + "? ")
                
            if int(RasAns) == prod:
                print("Vastus on õige -- hästi.\n")
                correct += 1
            else:
                print("Ei, vastus on ",prod)
                    
else:
    print("Palun vali algaja või raske.\n")
            
            
    
print("\nMa küsisin sinult", küsimused, "küsimust. Sa said ", correct, " neist õigesti.")
    
if correct / küsimused > 2/3:
    print("hästi tehtud!\n")
elif correct / küsimused > 1/3:
    print("Sul on vaja harjutada.\n")
else:
    print("Sul on tõesti abi vaja, küsi õpetajatelt!\n")
        
restart = input("Kas sa soovid jälle proovida? Y/N: ")
if restart == "Y":
    continue
elif restart == "N":
    break
else:
    print("Palun vali Y või N")