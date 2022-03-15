#Simo Andreas Novikov
#10.03.2022


import random
correct = 0
game = 1
kusimused = 10

while game==1:
    for i in range(kusimused):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        arv = random.randint(1, 2)
        if arv==1:
            liitmine=num1 + num2
            vastus = int(input(f"{num1}+{num2}= "))
            if int(vastus) == liitmine:
                print("Õige")
                correct += 1
            else:
                print("Vale")
                
        if arv==2:
            lahutamine=num1 - num2
            vastus = int(input(f"{num1}-{num2}= "))
            if int(vastus) == lahutamine:
                print("Õige")
                correct += 1
            else:
                print("Vale")
                
    print("Sinult küsiti", kusimused, "küsimust. Sa said", correct, "neist õigesti.")

    if correct / kusimused > 0.63:
        print(f"tulemus: {(correct/kusimused)*100}%. Hästi tehtud!")
    else:
        print(f"tulemus: {(correct/kusimused)*100}%. Sul on abi vaja!")
        

    valik=input("Kas soovid jätkata? (j/e)")
    if valik == "e":
        game=0
print("Tänan mängimast!")
