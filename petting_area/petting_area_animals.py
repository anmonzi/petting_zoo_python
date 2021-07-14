# import the python datetime module to help us create a timestamp
from datetime import date



# Walking animals

class Llama:

    def __init__(self, name, species, shift):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning")
print(miss_fuzz.name)

class Goat:

    def __init__(self, name, species, shift):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

lady_goat = Goat("The G.O.A.T", "domestic goat", "morning")
print(lady_goat.name)

class Donkey:

    def __init__(self, name, species, shift):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

donkey = Donkey("Donkey", "domestic donkey", "midday")
print(donkey.name)

class Pony:

    def __init__(self, name, species, shift):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

little_pony = Pony("Princess", "domestic pony", "afternoon")
print(little_pony.name)

class Alpaca:

    def __init__(self, name, species, shift):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

silver_bullet = Alpaca("Silver Bullet", "domestic alpaca", "afternoon")
print(f"{silver_bullet.name} the {silver_bullet.species} is available to pet during the {silver_bullet.shift} shift.")