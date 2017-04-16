# -*- coding: utf-8 -*-

import random

# Här har vi ett slimemonster
slimenr = 0
class Slime(object):
    def __init__(self):
        global slimenr
        slimenr = slimenr + 1
        self.name = "Slime"
        self.strength = 2 + int(random.random()*11)
        self.defence = 0
        self.hp = 25 + int(random.random()*11)
    def fight(self, hero):
        while self.hp > 0 and hero.hp > 0:
            if int(random.random() * 101) < 90:
                if hero.weapon.ability == "fire":
                    self.hp = self.hp - 10 - hero.weapon.dmg
                    print ("Damage done: " + str(10 + hero.weapon.dmg) 
                           + ", hp left: " + str(self.hp) + ". Keep going!")
                else:
                    self.hp = self.hp - 1 - int(hero.weapon.dmg*0.2)
                    print ("Damage done: " + str(1 + int(hero.weapon.dmg*0.2))
                           + ", hp left: " + str(self.hp) 
                           + ". It doesn't seem to go that well")
            else:
                print "You missed"
            if self.hp > 0 and hero.hp > 0:
             # Ifall den redan dött ska vi ej fortsätta här!
                if int(random.random() * 101) < 90:
                    hero.hp = hero.hp - self.strength
                    print ("The acid burns your skinn! You have " + str(hero.hp)
                           + " hp left!")
                else:
                    print "The monster missed"
            print ('The fight is going on... you can either stay and fight'
                   + ', change your weapon or run away! If you want to stay'
                   + ' and fight, type "fight". If you want to change your weapon'
                   +', type "weapon". If you want to run away from the fight, '
                   + 'type "run"')
            while True:
                choice = raw_input("What do you choose to do?")
                if choice == "fight":
                    break
                     # "break" gör att man kommer ut ur befintlig loop (bara i
                     # while och for loop)
                elif choice == "weapon":
                    hero.showinventory()
                    choice = raw_input("What weapon do you want to use?")
                    hero.setweapon(choice)
                    break
                elif choice == "run":
                    return 
                     # "return" gör slut på nuvarande funktion. och den kan skicka
                     # tillbaka ett värde
                else:
                    print "Wrong choice"
        if self.hp > hero.hp:
            print "You are dead!"
        else:
            print "You won!"


# Här har vi en slimeking 
slimeking = 0
class Slimeking(Slime):
    def __init__(self):
        global slimekingnr
        slimekingnr = slimekingnr + 1
        self.name = "Slimeking"
        self.strength = 10 + int(random.random() * 11)
        self.defence = 0
        self.hp = 60 + int(random.random() * 11)
            

# Här har vi vapen
class Weapon(object):
    def __init__(self, name, dmg, ability):
        self.name = name
        self.dmg = dmg
        self.ability = ability
        
excalibur = Weapon("Excalibur", 20, "stonecutter")
glowstick = Weapon("Glowstick", 15, "fire")
icicle = Weapon("Icicle", 7, "freeze")
dullknife = Weapon("Dull knife", 5, "tickle")
sabre = Weapon("Sabre", 10, "slice")

# Här har vi en hero
class Hero(object):
    def __init__(self, name, strength, defence, hp):
        self.name = name
        self.strength = strength
        self.defence = defence
        self.hp = hp
        self.inventory = [dullknife]
        self.weapon = dullknife
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


testslime = Slime()
me = Hero("Me", 30, 30, 30)
testslime.fight(me)


skeletonnr = 0
class skeleton(object):
    def __init__(self):
        global skeletonnr
        skeletonnr=skeletonnr + 1
        self.name = "Skeleton: " + str(skeletonnr)
        self.strength = 10 + int(random.random()*11)
        self.defence = 10 + int(random.random()*11)
        self.hp = 30 + int(random.random()*11)

    










[Weapon("Excalibur", 20, "stonecutter"),
                          Weapon("Glowstick", 15, "fire"),
                          Weapon("Icicle", 7, "freeze")]
