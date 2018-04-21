import random
import pandas as pd        #this is the excel stuff
import Dictionaries as D
import importlib

D = importlib.reload(D) #This is for updating changes to the Dictionaries file

#Character Generator v0.1, 11 hours
'''
This program is made for generating a random Dungeons and Dragons 5th edition. As of right now, it makes only a 1st level character.
There are 3 settings: 
1) A purely random generator. 
2) A psuedorandom generator that asks you at every step whether you want to choose or have it be random. 
3) A questoinaire that sends you through a question tree to decide your character traits.
'''

# Level = 0
# Race = ""
# Class = ""
# Background = ""
# Alignment = ""
# Abilities = []
# Feats = []
# Skills = []
# trSkills = []
# Languages = []
# profBonus = 0
# HP = 0
# Initiative = 0
# Speed = 0


def Random():
    '''The Random Function will make a level 1 character at complete random.'''
    
    '''This is resetting all of the key varaibles'''
    Level = 0
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
    Size = ''
    
    '''Random level setter'''
    Level = random.randint(1,1)
    
    '''This will randomly deciding Abilities'''
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
    
    '''This will randomly deciding Background'''
    r = random.randint(0,len(D.loBackground)-1)
    Background = D.loBackground[r]
    bt = BackgroundTraits(Background, Feats, trSkills, Prof)
    s = getattr(bt, Background)()
    Background = s[0]
    Feats = s[1]
    trSkills = s[2]
    Prof = s[3]
    
    '''This will randomly deciding Class'''
    r = random.randint(0,len(D.loClass)-1)
    Class = D.loClass[r]
    ct = ClassTraits(Class, Abilities, Feats, trSkills, Prof, HP, Speed, Level)
    s = getattr(ct, Class)()
    Class = s[0]
    Abilities = s[1]
    Feats = s[2]
    trSkills = s[3]
    Prof = s[4]
    HP = s[5]
    Speed = s[6]
    
    '''This will randomly deciding Race'''
    #r = random.randint(0,len(D.loRace)-1)
    r = random.randint(0,1)
    Race = D.loRace[r]
    rt =  RacialTraits(Race, Abilities, Feats, trSkills, Prof, HP, Speed, Level, Languages, Size)  
    s = getattr(rt, Race)()
    Race = s[0]
    Abilities = s[1]
    Feats = s[2]
    trSkills = s[3]
    Prof = s[4]
    HP = s[5]
    Speed = s[6]
    Level = s[7]
    Languages = s[8]
    Size = s[9]    
    
    '''This will randomly decide the alignment of the Character.'''
    Alignment = D.Alignments[random.randint(0,8)]
    
    print(Race + '        ' + Class + '        ' + Background + '        ' + Size)
    print(Abilities)
    print(Feats)
    print(trSkills)
    print(Prof)
    print(HP)
    print(Speed)
    print(Alignment)
    print(Languages)
    
    # for i in range(0,len(trSkills)):
    #     print(D.Skills[trSkills[i]])
    
   
class RacialTraits(object):
    '''This class is for adding the racial traits to the Character''' 
    def __init__(self, Race, Abilities, Feats, trSkills, Prof, HP, Speed, Level, Languages, Size):
        self.Race = Race
        self.Abilities = Abilities
        self.Feats = Feats
        self.trSkills = trSkills
        self.Prof = Prof
        self.HP = HP
        self.Speed = Speed
        self.Level = Level
        self.Languages = Languages
        self.Size = Size
        
        
    def Dwarf(self):        
        self.Abilities[2] += 2
        self.Speed = 25
        self.Size = 'Medium'
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Dwarvish',self.Languages)
        f = ['Darkvision','Dwarven Resilience','Dwarven Combat Training','Tool Proficiency (Dwarven)', 'Stonecunning']   
        if random.randint(0,2) == 0:
            self.Race = "Hill_Dwarf"
            self.Abilities[4] += 1
            self.HP += (self.Level*1)
            f.append('Dwarven Toughness')
        else:
            self.Race = "Mountain_Dwarf"
            self.Abilities[0] += 2
            self.Prof.append("light armor")
            self. Prof.append('medium armor')
            f.append('Dwarven Armor Training')
        for i in range(0,len(f)):
            self.Feats = addFeat(f[i],self.Feats)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Elf(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Elvish',self.Languages)
        self.Abilities[1] += 2
        self.Speed = 30
        self.Size = 'Medium'
        f = ['Darkvision','Keen Senses','Fey Ancestry','Trance']
        r= random.randint(0,2)
        if r == 0:
            self.Race = 'High_Elf'
            self.Abilities[3] += 1
            self.Languages = addLanguage('Common',self.Languages)
            f.append('Elf Weapon Training')
            f.append('Cantrip (High Elf)')
        if r == 1:
            self.Race = 'Wood_Elf'
            self.Abilities[4] += 1
            f.append('Elf Weapon Training')
            f.append('Fleet of Foot')
            self.Speed = 35
            f.append('Mask of the Wild')
        if r == 2:
            self.Race = 'Dark_Elf'
            self.Abilities[5] += 1
            f.append('Superior Darkvision')
            f.append('Sunlight Sensitivity')
            f.append('Drow Magic')
            f.append('Drow Weapon Training')
        for i in range(0,len(f)):
            self.Feats = addFeat(f[i],self.Feats)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Halfling(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Halfling',self.Languages)
        self.Abilities[1] += 2
        self.Speed = 25
        self.Size = 'Small'
        f = ['Lucky','Brave','Halfling Nimbleness']
        r = random.randint(0,1)
        if r == 0:
            self.Race = 'Lightfoot_Halfling'
            self.Abilities[5] += 1
            f.append('Naturally Stealthy')
        if r == 1:
            self.Race = 'Stout_Halfling'
            self.Abilities[2] += 1
            f.append('Stout Resilience')
        for i in range(0,len(f)):
            self.Feats = addFeat(f[i],self.Feats)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Human(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Common',self.Languages)
        self.Speed = 30
        self.Size = 'Medium'
        for i in range(0,5):
            self.Abilities[i] += 1
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Dragonborn(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Draconic',self.Languages)
        self.Abilities[0] += 2
        self.Abilities[5] += 1
        self.Speed = 30
        f = ['Draconic Ancestry','Breath Weapon','Damage Resistance (Dragonborn)']
        for i in range(0,len(f)):
            self.Feats = addFeat(f[i],self.Feats)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Gnome(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Gnomish',self.Languages)
        self.Abilities[3] += 2
        f = ['Darkvision','Gnome Cunning']
        r = random.randint(0,1)
        if r == 0:
            self.Race = 'Forest_Gnome'
            self.Abilities[1] += 1
            f.append('Natural Illusionist')
            f.append('Speak With Beaasts')
        if r == 1:
            self.Race = 'Rock_Gnome'
            self.Abilities[2] +=1
            f.append('Artificer\'s Lore')
            f.append('Tinker')
        for i in range(0,len(f)):
            self.Feats = addFeat(f[i],self.Feats)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Half_Elf(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Elvish',self.Languages)
        self.Languages = addLanguage('Common',self.Languages)
        f = ['Darkvision','Fey Ancestry']
        self.Abilities[5] += 2
        r = random.randint(0,4)
        self.Abilities[r] += 1
        t = True
        while t == True:
            k = random.randint(0,4)
            if k != r:
                self.Abilities[k] += 1
                t = False
        for i in range(0,len(f)):
            self.Feats = addFeat(f[i],self.Feats)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Half_Orc(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Orcish',self.Languages)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Tiefling(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Infernal',self.Languages)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Aasimar(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Celestial',self.Languages)
        r = random.randing(0,2)
        if r ==0:
            self.Race = 'Protector_Aasimar'
        if r == 1:
            self.Race = 'Scourge_Aasimar'
        if r == 2:
            self.Race = 'Fallen_Aasimar'
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Firblog(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Elvish',self.Languages)
        self.Languages = addLanguage('Giant',self.Languages)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Goliath(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Giant',self.Languages)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Kenku(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Auran',self.Languages)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Lizardfolk(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Draconic',self.Languages)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Tabaxi(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Common',self.Languages)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Triton(self):
        self.Languages = addLanguage('Common',self.Languages)
        self.Languages = addLanguage('Primordial',self.Languages)
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
        
    def Monstrous(self):
        print('ughhhhhhhhhhhhhhhhhhhhhhh')
        return(self.Race, self.Abilities, self.Feats, self.trSkills, self.Prof, self.HP, self.Speed, self.Level, self.Languages, self.Size)
    
        
   
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
    
def addLanguage(Language, Languages):
    t = True
    if Language not in Languages:
        Languages.append(Language)
    else:
        while t == True:
            r = random.randint(0,14)
            if D.loLanguages[r] not in Languages:
                Languages.append(D.loLanguages[r])
                t = False
    return Languages
    
def addFeat(Feat, Feats):
    if Feat not in Feats:
        Feats.append(Feat)
    return Feats
        
