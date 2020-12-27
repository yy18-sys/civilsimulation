import time

class human:

    def __init__(self, name,maxhealth,health,maxfood,food):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health
        self.maxfood = maxfood
        self.food = food
        self.alive = True

    def setDamage(self, damage):
        currentHealth =  self.health - damage
        if currentHealth <= 0:
            self.alive = False
        else:
            if currentHealth > self.maxhealth:
                self.health = self.maxhealth
            else:
                self.health = currentHealth

    def addFood(self, food):
        currentFood = self.food - food
        if currentFood <= 0:
            self.alive = False
        else:
            if currentFood > self.maxfood:
                self.food = self.maxfood
            else:
                self.food = currentFood

    def getFood(self):
        return self.food

    def getHealth(self):
        return self.health

    def isAlive(self):
        return self.alive