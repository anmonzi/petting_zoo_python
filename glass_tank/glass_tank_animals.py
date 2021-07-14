# import the python datetime module to help us create a timestamp
from datetime import date



# Slithering animals

class Copperhead:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = True

copperhead = Copperhead("Dan", "venomous snake")
print(f"The copperhead {copperhead.name}, is venomous? {copperhead.venomous}")

class KingCobra:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = True

king_cobra = KingCobra("Slytherin", "venomous snake")
print(king_cobra.venomous)

class RatSnake:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = False

rat_snake = RatSnake("Basil", "non-venomous snake")
print(rat_snake.slithering)

class GiantAnaconda:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = False

anaconda = GiantAnaconda("Jafaar", "boa constrictor")
print(anaconda.species)

class Cottonmouth:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = True

cottonmouth = Cottonmouth("Medusa", "venomous snake")