class Attraction:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)

    @property
    def last_critter_added(self):
        return f"{self.animals[-1]} and was the last animal added"