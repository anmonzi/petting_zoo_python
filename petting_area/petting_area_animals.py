# import the python datetime module to help us create a timestamp
from datetime import date



# Walking animals

class Llama:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

miss_fuzz = Llama("Miss Fuzz", "domestic llama")
print(miss_fuzz.name)

class Goat:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

lady_goat = Goat("The G.O.A.T", "domestic goat")
print(lady_goat.name)

class Donkey:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

donkey = Donkey("Donkey", "domestic donkey")
print(donkey.name)

class Pony:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

little_pony = Pony("Princess", "domestic pony")
print(little_pony.name)

class Alpaca:

    def __init__(self, name, species):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

silver_bullet = Alpaca("Silver Bullet", "domestic alpaca")
print(silver_bullet.name)