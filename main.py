import random

class Wizard:
    def __init__(self, name, max_health):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.mana = 100
        self.alive = True
        self.spells = ["fireball", "lightning bolt", "heal", "curse", "shield", "poison", "teleport", "charm", "invisibility", "summon"]

    def __str__(self):
        return f"{self.name}: {self.health}/{self.max_health} HP, {self.mana} Mana" 

    def attack(self, other, spell):
        cost = 0
        damage = 0
        if spell not in self.spells:
            print(f"{self.name} doesn't know that spell!")
            return
        if spell == "fireball":
            damage = random.randint(20, 30)
            cost = 10
        elif spell == "lightning bolt":
            damage = random.randint(30, 50)
            cost = 15
        elif spell == "heal":
            if self.health == self.max_health:
                print(f"{self.name} is already at full health!")
                return
            heal = random.randint(20, 30)
            self.health = min(self.health + heal, self.max_health)
            cost = 5
            print(f"{self.name} healed for {heal} points.")
            return
        elif spell == "curse":
            if not other.alive:
                print(f"{other.name} is already dead!")
                return
            other.health -= 5
            if other.health <= 0:
                other.health = 0
                other.alive = False
                print(f"{other.name} has been cursed and has died.")
                return
            elif spell == "shield":
                self.health += 5
                cost = 5
                print(f"{self.name} reinforced their shield.")
                return
            elif spell == "poison":
                if not other.alive:
                    print(f"{other.name} is already dead!")
                    return
                other.health -= 5
                if other.health <= 0:
                    other.health = 0
                    other.alive = False
                    print(f"{other.name} has been poisoned and has died.")
                else:
                    print(f"{other.name} has been poisoned.")
                return
            elif spell == "teleport":
                self.health -= 5
                cost = 5
                print(f"{self.name} teleported and lost 5 health points.")
                return
            elif spell == "charm":
                if not other.alive:
                    print(f"{other.name} is already dead!")
                    return
                other.health = 0
                other.alive = False
                print(f"{other.name} has been charmed and has died.")
                return
            elif spell == "invisibility":
                self.health -= 5
                cost = 5
                print(f"{self.name} turned invisible and lost 5 health points.")
                return
            elif spell == "summon":
                self.health -= 5
                cost = 5
                print(f"{self.name} summoned a creature and lost 5 health points.")
                return
        if self.mana < cost:
            print(f"{self.name} doesn't have enough mana to cast that spell!")
            return
        self.mana -= cost
        if not other.alive:
            print(f"{other.name} is already dead!")
            return
        other.health -= damage
        if other.health <= 0:
            other.health = 0
            other.alive = False
            print(f"{other.name} has been defeated!")
        else:
            print(f"{self.name} hit {other.name} with a {spell} spell for {damage} points of damage.")

def duel(wizard1, wizard2):
    print(f"{wizard1.name} vs {wizard2.name}")
    while wizard1.alive and wizard2.alive:
        print()
        print(wizard1)
        print(wizard2)
        print()
        spell = input(f"{wizard1.name}, choose a spell: ")
        wizard1.attack(wizard2, spell)
        if not wizard2.alive:
            break
        spell = input(f"{wizard2.name}, choose a spell: ")
        wizard2.attack(wizard1, spell)

wizard1 = Wizard("Gandalf", 100)
wizard2 = Wizard("Sauron", 100)
duel(wizard1, wizard2)
