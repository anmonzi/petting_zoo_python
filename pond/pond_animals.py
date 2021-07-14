# import the python datetime module to help us create a timestamp
from datetime import date


# Swimming


class Goldfish:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = False
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Stonefish:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Mallard:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = False
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class BlueRingedOctopus:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class BoxJellyfish:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.venomous = True
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

