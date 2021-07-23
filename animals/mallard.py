from animals import Animal
from movements import Walking, Swimming

# Designate Goat as a child class by adding (Animal) after the class name
class Mallard(Animal, Walking, Swimming):
    # Remove redundant properties from Goat's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        Walking.__init__(self)
        Swimming.__init__(self)
        # Establish the propertis of each animal with a default value
        self.venomous = False

    def quack(self):
        print("The mallard quacks! A lot!")

    # run is defined in the Walking parent class, but also here. This run method will take precedence and Walking's run method will not be called by Goose instances
    def run(self):
        print(f'{self} waddles')

    def swim(self):
        print(f'{self} uses his webbed feet to swim.')

    def __str__(self):
        return f'{self.name} the mallard duck'