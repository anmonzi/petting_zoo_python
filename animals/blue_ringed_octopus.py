from animals import Animal
from datetime import date

# Designate Goat as a child class by adding (Animal) after the class name
class BlueRingedOctopus(Animal):
    # Remove redundant properties from Goat's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        # Establish the propertis of each animal with a default value
        self.swimming = True
        self.venomous = True
    
    def feed(self):
        print(f'{self.name} was not fed {self.food} on {date.today().strftime("%m/%d/%Y")} because there\'s a shortage of crab.')