from .attraction import Attraction

class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.append(animal)
                print(f'{animal} now lives in {self.name}')
        except AttributeError:
                print(f'{animal} doesn\'t swim, nor does it belong in the {self.name} attraction.')