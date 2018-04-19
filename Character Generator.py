import random
import pandas as pd
import FeatDictionary

#Character Generator v0.1, 7 hours
'''
This program is made for generating a random Dungeons and Dragons 5th edition. As of right now, it makes only a 1st level character.
There are 3 settings: 
1) A purely random generator. 
2) A psuedorandom generator that asks you at every step whether you want to choose or have it be random. 
3) A questoinaire that sends you through a question tree to decide your character traits.
'''

Level = 0
Race = ""
Class = ""
Background = ""
Alignment = ""
Abilities = []
Feats = []
Skills = []
trSkills = []
Languages = []
profBonus = 0
HP = 0
Initiative = 0
Speed = 0


def Random():
    '''The Random Function will make a level 1 character at complete random.'''
    
    '''This is resetting all of the key varaibles'''
    Level = 1
    Race = ""
    Class = ""
    Background = ""
    Alignment = ""
    Abilities = []
    Feats = []
    Skills = []
    trSkills = []
    Prof = []
    Languages = []
    profBonus = 2
    HP = 0
    Initiative = 0
    Speed = 0
    
    '''This is the randomly deciding Abilities'''
    for i in range(0,6):
        d6s = []
        a = 0
        for i in range(0,4):
            d6s.append(random.randint(1,6))
        d6s = sorted(d6s)
        d6s = d6s[1:4]
        for i in range(0,3):
            a += d6s[i]
        Abilities.append(a)
    
    '''This is the randomly deciding Background'''
    loBackground = ['Acolyte','Charlatan','Criminal','Entertainer','Folk_Hero','Guild_Artisan','Hermit','Noble','Outlander','Sage','Sailor','Soldier','Urchin']
    r = random.randint(0,len(loBackground)-1)
    Background = loBackground[r]
    bt = BackgroundTraits(Background, Feats, trSkills, Prof)
    s = getattr(bt, Background)()
    Background = s[0]
    Feats = s[1]
    trSkills = s[2]
    Prof = s[3]
    
    '''This is the randomly deciding Class'''
    loClass = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
    r = random.randint(0,len(loClass)-1)
    #r = 0
    Class = loClass[r]
    ct = ClassTraits(Class, Abilities, Feats, trSkills, Prof, HP, Speed, Level)
    s = getattr(ct, Class)()
    Class = s[0]
    Abilities = s[1]
    Feats = s[2]
    trSkills = s[3]
    Prof = s[4]
    HP = s[5]
    Speed = s[6]
    
    '''This is the randomly deciding Race'''
    loRace = ['Dwarf','Elf','Halfling','Human','Dragonborn','Gnome','Half_Elf','Half_Orc','Tiefling','Aasimar','Firblog','Goliath','Kenku','Lizardfolk','Tabaxi','Triton','Monstrous']
    r = random.randint(0,len(loRace)-1)
    #r = 0
    Race = loRace[r]
    rt =  RacialTraits(Race, Abilities, Feats, trSkills, Prof, HP, Speed, Level)  
    s = getattr(rt, Race)()
    Race = s[0]
    Abilities = s[1]
    Feats = s[2]
    trSkills = s[3]
    Prof = s[4]
    HP = s[5]
    Speed = s[6]    
    
    '''This will randomly decide the alignment of the Character.'''
    Alignments = ['Lawful Good','Neutral Good','Chaotic Good','Lawful Neutral','True Neutral','Chaotic Neutral','Lawful Evil','Neutral Evil','Chaotic Evil']
    Alignment = Alignments[random.randint(0,8)]
    
    
    print(Race)
    print(Class)
    print(Background)
    print(Abilities)
    print(Feats)
    print(trSkills)
    print(Prof)
    print(HP)
    print(Speed)
    print(Alignment)
    
   
class RacialTraits(object):
    '''This class is for adding the racial traits to the Character''' 
    def __init__(self, Race, Abilities, Feats, trSkills, Prof, HP, Speed, Level):
        self.Race = Race
        self.Abilities = Abilities
        self.Feats = Feats
        self.trSkills = trSkills
        self.Prof = Prof
        self.HP = HP
        self.Speed = Speed
        self.Level = Level
        
    def Dwarf(self):        
        self.Abilities[2] += 2
        self.Speed += 25
        if random.randint(0,2) == 0:
            self.Race = "Hill_Dwarf"
            self.Abilities[4] += 1
            self.HP += (Level*1)
        else:
            self.Race = "Mountain_Dwarf"
            self.Abilities[0] += 2
            self.Prof.append("light armor")
            self. Prof.append('medium armor')
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Elf(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Halfling(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Human(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Dragonborn(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Gnome(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Half_Elf(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Half_Orc(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Tiefling(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Aasimar(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Firblog(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Goliath(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Kenku(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Lizardfolk(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Tabaxi(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Triton(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Monstrous(self):
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
    
        
   
class ClassTraits(object):
    '''This class is for adding the Class traits, and organizing the abilities.''' 
    def __init__(self, Class, Abilities, Feats, trSkills, Prof, HP, Speed, Level):
        self.Class = Class
        self.Abilities = Abilities
        self.Feats = Feats
        self.trSkills = trSkills
        self.Prof = Prof
        self.HP = HP
        self.Speed = Speed
        self.Level = Level
        
    def Barbarian(self):
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = STRabl(self.Abilities)
        self.HP += 12    
        self.trSkills.append(0)
        self.trSkills.append(2)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Bard(self): 
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = CHAabl(self.Abilities)
        self.HP += 8
        self.trSkills.append(1)
        self.trSkills.append(5)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Cleric(self):
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = WISabl(self.Abilities)
        self.HP += 8
        self.trSkills.append(4)
        self.trSkills.append(5)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
         
    def Druid(self): 
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = WISabl(self.Abilities)
        self.HP += 8
        self.trSkills.append(3)
        self.trSkills.append(4)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Fighter(self): 
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        d = random.randint(0,1)
        if d == 0:
            self.Abilities = STRabl(self.Abilities)
        else:
            self.Abilities = DEXabl(self.Abilities)
        self.HP += 10
        self.trSkills.append(0)
        self.trSkills.append(2)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Monk(self): 
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = DEXabl(self.Abilities)
        self.HP += 8
        self.trSkills.append(0)
        self.trSkills.append(1)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Paladin(self): 
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = STRabl(self.Abilities)
        self.HP += 10
        self.trSkills.append(4)
        self.trSkills.append(5)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Ranger(self): 
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = DEXabl(self.Abilities)
        self.HP += 10
        self.trSkills.append(0)
        self.trSkills.append(1)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Rogue(self): 
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = DEXabl(self.Abilities)
        self.HP += 8
        self.trSkills.append(1)
        self.trSkills.append(3)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Sorcerer(self): 
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = CHAabl(self.Abilities)
        self.HP += 6
        self.trSkills.append(2)
        self.trSkills.append(5)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Warlock(self): 
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = CHAabl(self.Abilities)
        self.HP += 8
        self.trSkills.append(4)
        self.trSkills.append(5)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
    def Wizard(self):
        '''This is organizing the abilities based on the top class trait, then it is random.'''
        self.Abilities = INTabl(self.Abilities)
        self.HP += 6
        self.trSkills.append(3)
        self.trSkills.append(4)
        return(self.Class, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level)
        
class BackgroundTraits(object):
    '''This is the class for assigning all the traits related to their background.'''
    def __init__(self, Background, Feats, trSkills, Prof):
        self.Background = Background
        self.Feats = Feats
        self.trSkills = trSkills
        self.Prof = Prof
    
    def Acolyte(self): 
        self.trSkills.append(12)
        self.trSkills.append(20)
        self.Feats.append('Shelter of the Faithful')
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Charlatan(self): 
        self.trSkills.append(10)
        self.trSkills.append(21)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Criminal(self): 
        self.trSkills.append(10)
        self.trSkills.append(22)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Entertainer(self): 
        self.trSkills.append(6)
        self.trSkills.append(18)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Folk_Hero(self):
        self.trSkills.append(7)
        self.trSkills.append(23)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Guild_Artisan(self):
        self.trSkills.append(12)
        self.trSkills.append(19)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Hermit(self): 
        self.trSkills.append(15)
        self.trSkills.append(20)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Noble(self): 
        self.trSkills.append(11)
        self.trSkills.append(19)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Outlander(self): 
        self.trSkills.append(9)
        self.trSkills.append(23)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Sage(self): 
        self.trSkills.append(8)
        self.trSkills.append(11)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Sailor(self): 
        self.trSkills.append(9)
        self.trSkills.append(17)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Soldier(self): 
        self.trSkills.append(9)
        self.trSkills.append(13)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
        
    def Urchin(self):
        self.trSkills.append(21)
        self.trSkills.append(22)
        return(self.Background, self.Feats, self.trSkills, self.Prof)
    


def STRabl(Abilities):
    '''This sets the highest score as Strength'''
    abl = [0,0,0,0,0,0]
    abl[0] = max(Abilities)
    Abilities.remove(max(Abilities))
    r = random.randint(0,len(Abilities)-1)
    abl[1] = Abilities[r]
    Abilities.remove(abl[1])
    r = random.randint(0,len(Abilities)-1)
    abl[2] = Abilities[r]
    Abilities.remove(abl[2])
    r = random.randint(0,len(Abilities)-1)
    abl[3] = Abilities[r]
    Abilities.remove(abl[3])
    r = random.randint(0,len(Abilities)-1)
    abl[4] = Abilities[r]
    Abilities.remove(abl[4])
    r = random.randint(0,len(Abilities)-1)
    abl[5] = Abilities[r]
    Abilities.remove(abl[5])
    return(abl)
        
def DEXabl(Abilities):
    '''This sets the highest score as Dexterity'''
    abl = [0,0,0,0,0,0]
    abl[1] = max(Abilities)
    Abilities.remove(max(Abilities))
    r = random.randint(0,len(Abilities)-1)
    abl[0] = Abilities[r]
    Abilities.remove(abl[0])
    r = random.randint(0,len(Abilities)-1)
    abl[2] = Abilities[r]
    Abilities.remove(abl[2])
    r = random.randint(0,len(Abilities)-1)
    abl[3] = Abilities[r]
    Abilities.remove(abl[3])
    r = random.randint(0,len(Abilities)-1)
    abl[4] = Abilities[r]
    Abilities.remove(abl[4])
    r = random.randint(0,len(Abilities)-1)
    abl[5] = Abilities[r]
    Abilities.remove(abl[5])
    return(abl)
        
def INTabl(Abilities):
    '''This sets the highest score as Intelligence'''
    abl = [0,0,0,0,0,0]
    abl[3] = max(Abilities)
    Abilities.remove(max(Abilities))
    abl[2] = max(Abilities)
    Abilities.remove(max(Abilities))
    r = random.randint(0,len(Abilities)-1)
    abl[1] = Abilities[r]
    Abilities.remove(abl[1])
    r = random.randint(0,len(Abilities)-1)
    abl[0] = Abilities[r]
    Abilities.remove(abl[0])
    r = random.randint(0,len(Abilities)-1)
    abl[4] = Abilities[r]
    Abilities.remove(abl[4])
    r = random.randint(0,len(Abilities)-1)
    abl[5] = Abilities[r]
    Abilities.remove(abl[5])
    return(abl)
    
def WISabl(Abilities):
    '''This sets the highest score as Wisdom'''
    abl = [0,0,0,0,0,0]
    abl[4] = max(Abilities)
    Abilities.remove(max(Abilities))
    r = random.randint(0,len(Abilities)-1)
    abl[1] = Abilities[r]
    Abilities.remove(abl[1])
    r = random.randint(0,len(Abilities)-1)
    abl[2] = Abilities[r]
    Abilities.remove(abl[2])
    r = random.randint(0,len(Abilities)-1)
    abl[3] = Abilities[r]
    Abilities.remove(abl[3])
    r = random.randint(0,len(Abilities)-1)
    abl[0] = Abilities[r]
    Abilities.remove(abl[0])
    r = random.randint(0,len(Abilities)-1)
    abl[5] = Abilities[r]
    Abilities.remove(abl[5])
    return(abl)
        
def CHAabl(Abilities):
    '''This sets the highest score as Charisma'''
    abl = [0,0,0,0,0,0]
    abl[5] = max(Abilities)
    Abilities.remove(max(Abilities))
    r = random.randint(0,len(Abilities)-1)
    abl[1] = Abilities[r]
    Abilities.remove(abl[1])
    r = random.randint(0,len(Abilities)-1)
    abl[2] = Abilities[r]
    Abilities.remove(abl[2])
    r = random.randint(0,len(Abilities)-1)
    abl[3] = Abilities[r]
    Abilities.remove(abl[3])
    r = random.randint(0,len(Abilities)-1)
    abl[4] = Abilities[r]
    Abilities.remove(abl[4])
    r = random.randint(0,len(Abilities)-1)
    abl[0] = Abilities[r]
    Abilities.remove(abl[0])
    return(abl)
        