##Zadanie 3
#
class member:
    team = 'KNMF'
    
    def __init__(self,imie,miedziaki,zadania):
        self.name = str(imie)
        self.cash = bool(miedziaki)
        self.exercise = float(zadania)
        
    def good_job(self,number = 1):
        self.exercise = self.exercise + float(number) 
    
    def new_team(self,new): #opcjonalne - drugi sposób
        self.team  = str(new)
    
    def __str__(self):
        return ('Mam na imie {} i jestem członkiem {}' .format(self.name,self.team) + '\n' +
                'Stan:' + '\n' + 'Zrobione zadania {}' .format(self.exercise) + '\n' +
                'Zapłacona składka {}.' .format(self.cash))              
        
        

czlowiek = member('Drozd', True,5)
print(czlowiek)

czlowiek.good_job()
czlowiek.team = 'Gwiezdna floata B540' 
print(czlowiek)

czlowiek.good_job(5)
czlowiek.new_team('Robak 2.0') 
print(czlowiek)

# Zadanie 4
        
class ranger(member):
    
    def __init__(self,imie,miedziaki,zadania,pseudonim):
        member.__init__(self,imie,miedziaki,zadania)
        self.nick_name = str(pseudonim)

    def __str__(self):
        return member.__str__(self) + '\n' + 'Pseudonim: {}' .format(self.nick_name)
        

czlowiek2 = ranger('Hanibal',False,0,'Psychopata')
print(czlowiek2)

czlowiek2.good_job(5) #zliczanie zadań dziwdziczy z klasy member
print(czlowiek2)




