# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name 
#         self.position = position
#         self.salrary = salary
#     def introduce(self):
#         print(f"Name: {self.name}.")

# employee1 = Employee("Ezio", "Game Developer", 1000_000 )

class Fruit:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def describe(self):
        print(f"Name: {self.name}.\n Color: {self.color}.\n Price: {self.price}.")
        
fruit1 = Fruit("apple", "red", 1000)
fruit2 = Fruit("orange", "orange", 500)
friut3 = Fruit("banana", "yellow", 2000)

# Fruits.describe(fruit1)

class Animal:
    def __init__(self, name, color, gender, energy = 100, hunger = 100):
        self.name = name
        self.color = color
        self.gender = gender
        self.hunger = hunger
        self.energy = energy
    def describe(self):
        print(f"Name: {self.name}.\n Color: {self.color}.\n Gender: {self.gender}.\n Energy: {self.energy}. Hunger: {self.hunger}")
    def sleep(self):
        self.hunger -= 50
        self.energy += 100
    def eat(self):
        self.hunger += 50
    def stat(self):
        print(f"Current energy: {self.energy}")

    
animal1 = Animal("tiger", "orange", "male",)


