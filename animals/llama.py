from animals import Animal
from datetime import date

# Designate Llama as a child class by adding (Animal) after the class name
class Llama(Animal):
    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_number):
        super().__init__(name, species, food, chip_number)
        # Establish the different propertis of each animal with a default value
        self.walking = True
        self.shift = shift  # stays on because not all animals have shifts

    def feed(self):
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')