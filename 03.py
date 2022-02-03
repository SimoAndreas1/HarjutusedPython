#harjutus 3
#Simo Andreas Novikov
#01.02.2022

'''
#korralik kasutajanimi
nimi = input("Sisesta nimi: ")
nimi = nimi.capitalize().strip()
print("Tere "+nimi+"!")


#vandumine
vanne = input("Ära kurat ütle: ")
vanne = vanne.lower().replace("kurat","***")
print(vanne)
'''
#emaili kontroll
#TRUE/FALSE  in/not in








#palindroom
sisestus = input("sisesta palindroom: ")
print(sisestus == sisestus[::-1]) 
      




#tundide ajad
'''
start = input("algusaeg: ")
lopp = input("lopuaeg: ")
hh1, mm1 = start.split(":")
hh2, mm2 = lopp.split(":")
minutid = int(hh1)*60+int(mm1)
minutid2 = int(hh2)*60+int(mm2)
#absoluutväärtus
ajavahe = abs(minutid-minutid2)
#teisendamine hh:mm
hh = ajavahe // 60 #täisarvuline jagamine
mm = ajavahe % 60 #jääk
#lausevormindamine format abil
print(f"Õpilase päeva pikkus on {hh}:{mm}")
'''








