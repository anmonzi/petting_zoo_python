from animals import Animal
from movements import Slithering

# Designate Goat as a child class by adding (Animal) after the class name
class Cottonmouth(Animal, Slithering):
    # Remove redundant properties from Goat's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        Slithering.__init__(self)
        # Establish the propertis of each animal with a default value
        self.venomous = True