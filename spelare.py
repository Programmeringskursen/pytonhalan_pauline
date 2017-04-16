class Hero(object):
    def __init__(self, name, strength, defence, hp):
        self.name = name
        self.strength = strength
        self.defence = defence
        self.hp = hp
        self.inventory = [Weapon("Excalibur", 20, "stonecutter"),
                          Weapon("Glowstick", 15, "fire"),
                          Weapon("Icicle", 7, "freeze")]
        self.weapon = False
    def showinventory(self):
        print 
    def setweapon(self, weaponname):
        self.weapon = "Excalibur"
    def __str__(self):
        return(self.name + ":  Strength:" + str(self.strength) 
               + " Defence:" + str(self.defence) + " Hp:" + str(self.hp))
    def attack(self, what): pass

            
hannes = Hero("Hannes", 5, 5, 20)
pauline = Hero("Pauline", 30, 30, 30)
thomas = Hero("Thomas", 100, 100, 100)
bastian = Hero("Bastian", 30, 50, 30)


class Weapon(object):
    def __init__(self, name, dmg, ability):
        self.name = name
        self.dmg = dmg
        self.ability = ability
        

excalibur = Weapon("Excalibur", 20, "stonecutter")
glowstick = Weapon("Glowstick", 15, "fire")
icicle = Weapon("Icicle", 7, "freeze")
dullknife = Weapon("Dull knife", 5 "tickle")
sabre = Weapon("Sabre", 10 "slice")
        
#attack        
        for obj in self.inventory:
            what.attack(self, obj)
            
            
            
            obj.attack(self, what)
        

    
