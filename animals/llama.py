# The package syntax is what allows for these clean import statements
from animals import Animal
from datetime import date
from movements import Walking

# Designate Llama as a child class by adding (Animal) after the class name
class Llama(Animal, Walking):
    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_number):
        Animal.__init__(self, name, species, food, chip_number)
        Walking.__init__(self)
        # Establish the different propertis of each animal with a default value
        self.shift = shift  # stays on because not all animals have shifts
        self.walk_speed = 5

    def feed(self):
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')

    def __str__(self):
        return f'{self.name} the Llama'




# NOTE: When a class inherits from two parents you have to discard using 
# the super().__init__() syntax and explicitly invoke 
# the initialization method of both by name. You also need to pass self as an argument
# - something that is not needed when you use the super() abstraction.