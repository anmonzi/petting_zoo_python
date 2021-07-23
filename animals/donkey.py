from animals import Animal
from movements import Walking


class Donkey(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        Walking.__init__(self)
        # Establish the propertis of each animal with a default value
        self.shift = shift # stays on because not all animals have shifts