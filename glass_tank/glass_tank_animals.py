# import the python datetime module to help us create a timestamp
from datetime import date



# Slithering animals

class Copperhead:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class KingCobra:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class RatSnake:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = False
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class GiantAnaconda:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = False
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Cottonmouth:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.venomous = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

