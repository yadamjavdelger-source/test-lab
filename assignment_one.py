
import random

class Knight:
    def __init__(self, name, age, friendship = 10):
        self.name = name
        self.friendship = friendship
        self.age = age
    def knight_activities_good(self, princess):
        print(f"{self.name} Slays a dragon!")
        princess.friendship += 10
        print(f"{self.name}'s friendship with {princess.name} = {princess.friendship}.")
    def knight_activities_bad(self, princess):
        print(f"{self.name} trips and falls before {princess.name}!")
        princess.friendship -= 10



class Princess:
    def __init__(self, name, age, friendship = 10):
        self.name = name
        self.friendship = friendship
        self.age = age
    def princess_activities_good(self, knight):
        print(f"Prince {self.name} praises the knight😊")
        knight.friendship += 10
        print(f"Prince {self.name}'s friendship with {knight.name} = {knight.friendship}.")
    def princess_activities_bad(self, knight):
        print(f"Prince{self.name} mocks {knight.name}")
        knight.friendship -= 10


knight = Knight("Ezio", 20)
princess = Princess("Lilith", 23)


def endings_define(knight, princess):
    if random.choice(["good", "bad"]) == "good":
        knight.knight_activities_good(princess)
    else:
        knight.knight_activities_bad(princess)

    if random.choice(["good", "bad"]) == "good":
        princess.princess_activities_good(knight)
    else:
        princess.princess_activities_bad(knight)

    print(f"Knight friendship level: {knight.friendship}\n Princes friendship level: {princess.friendship}")

    if knight.friendship >= 20 and princess.friendship >= 20:
        print("They fall in love!!!")
    elif knight.friendship <= 0 or princess.friendship <= 0:
        print("They hate each other!!!")
    else:
        print("Nothing happens...")

endings_define(knight, princess)


    
