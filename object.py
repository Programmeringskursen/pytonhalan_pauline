# -*- coding: utf-8 -*-

import random

class Slime(object):
    def __init__(self):
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
                           + " left!")
                else:
                    print "The monster missed"
            print ('The fight is going on... you can either stey and fight'
                   + ', change your weapon or run away! If you want to stay'
                   + ' and fight, type "fight". If you want to change your weapon'
                   +', type "weapon". If you want to run away from the fight, '
                   + 'type "run"')
            choice = raw_input("What do you choose to do?")
            if choice == "fight":
            if choice == "weapon":
                hero.showinventory()
                choice = raw_input("What weapon do you want to use?")
                hero.setweapon(choice)
            if choice == "run":
        if self.hp > hero.hp:
            print "You are dead!"
        else:
            print "You won!"


class Slimeking(Slime):
    def __init__(self):
        self.name = "Slimeking"
        self.strength = 10 + int(random.random() * 11)
        self.defence = 0
        self.hp = 60 + int(random.random() * 11)
            

skeletonnr=0

class skeleton(object):
    skeletonnr=skeletonnr + 1
    def __init__(self):
        self.name = "Skeleton: " + str(skeletonnr)
        self.strength = 10 + int(random.random()*11)
        self.defence = 10 + int(random.random()*11)
        self.hp = 30 + int(random.random()*11)

    











