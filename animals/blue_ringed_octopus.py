from animals import Animal
from datetime import date
from movements import Swimming

# Designate Goat as a child class by adding (Animal) after the class name
class BlueRingedOctopus(Animal, Swimming):
    # Remove redundant properties from Goat's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        Swimming.__init__(self)
        # Establish the propertis of each animal with a default value
        self.venomous = True
    
    def feed(self):
        print(f'{self.name} was not fed {self.food} on {date.today().strftime("%m/%d/%Y")} because there\'s a shortage of crab.')