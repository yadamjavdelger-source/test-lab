# class Warrior:
#     def __init__(self, name, health = 75):
#         self.name = name
#         self.health = health
#     def attack(self):
#         print(f"{warrior1.name} attacks!")


       
# class Mage:
#     def __init__(self, name, health = 50):
#         self.name = name
#         self.health = health
#     def attack(self):
#         print(f"{mage1.name} attacks!")
       
# class Druid:
#     def __init__(self, name, health = 100):
#         self.name = name
#         self.health = health
#     def attack(self):
#         print(f"{druid1.name} attacks!")
        
# druid1 = Druid("Masha")
# warrior1 = Warrior("Ezio")
# mage1 = Mage("Mendee")

# druid1.attack()
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def heal(self):
        if self.health <= 100:
            self.health += 5
    def show_health(self):
        print(f"{self.name}'s health - {self.health}")

class Warrior(Character):
    def attack(self):
        print(f"Warrior {self.name} swings sword!")

class Mage(Character):
    def attack(self):
        print(f"Mage {self.name} uses magic!")

class Druid(Character):
    def attack(self):
        print(f"Druid {self.name} uses its claw!")

w = Warrior("Ezio", 75)
m = Mage("Alice", 50)
d = Druid("Masha", 100)

w.attack()
w.heal()
w.show_health()
m.show_health()
