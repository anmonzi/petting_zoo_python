from animals import Animal
from movements import Walking

# Designate Goat as a child class by adding (Animal) after the class name
class Goat(Animal, Walking):
    # Remove redundant properties from Goat's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self,name, species, food, chip_number)
        Walking.__init__(self)
        # Establish the propertis of each animal with a default value
        self.shift = shift  # stays on because not all animals have shifts
        self.walk_speed = 1

