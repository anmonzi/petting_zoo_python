# import the python datetime module to help us create a timestamp
from datetime import date


# Swimming


class Goldfish:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = False

goldfish = Goldfish("Milo", "fish")
print(f"The goldfish {goldfish.name}, is venomous? {goldfish.venomous}")

class Stonefish:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = True

stonefish = Stonefish("Fluffy", "venomous fish")

class Mallard:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = False

mallard = Mallard("Ricky", "bird")

class BlueRingedOctopus:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = True

octopus = BlueRingedOctopus("Atlantis", "octopus")

class BoxJellyfish:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = True

jellyfish = BoxJellyfish("Angel", "jellyfish")