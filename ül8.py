#Ülesanne 08
#Simo Andreas Novikov
#28.02.2022


class auto:
    #atribuudid
    automark = 'teadmata'
    aasta = 'teadmata'
    hind = 0
    
    
    
    #meetodid
    def __init__(self,x,y,z):
        self.automark = x
        self.aasta = y
        self.hind = z
        
        
    def kuva(self):
        print('mark: {} \nAasta: {}'.format(self.automark, self.aasta))
        
    def lisaHind(self,x):
        self.hind = x
        
    def kuvaHind(self):
        print('Hind: {}'.format(self.hind))
        
        
uusObjekt = auto("Audi", 2004, 45000)