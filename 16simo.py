#16. ülesanne
#Simo Andreas Novikov
#14.03.2022

import random


mängija1_score = 0
mängija2_score = 0


for i in range(10):
    
    mängija1_value = random.randint(1, 6)
    mängija2_value = random.randint(1, 6)
    
    print("Mängija1 veeretas: ", mängija1_value)
    print("Mängija2 veeretas: ", mängija2_value)
    
    
    if mängija1_value > mängija2_value:
        print("Mängija 1 võitis.")
        mängija1_score = mängija1_score + 1
    elif mängija2_value > mängija1_value:
        print("mängija 2 võitis")
        mängija2_score = mängija2_score + 1
    else:
        print("tuli viik")
        
    input("vajuta enter, et edasi minna")
    
print("### Mäng Läbi ###")
print("Mängija1 punktid: ", mängija1_score)
print("Mängija2 punktid: ", mängija2_score)