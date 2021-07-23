from animals import Animal

class Alpaca(Animal):

    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        # Establish the propertis of each animal with a default value
        self.walking = True
        self.shift = shift # stays on because not all animals have shifts