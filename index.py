from animals import Animal, Llama, Goat, Pony, Donkey, Alpaca, StoneFish, RatSnake, Mallard, KingCobra, GoldFish, GiantAnaconda, CopperHead, Cottonmouth, BoxJellyfish, BlueRingedOctopus
from attractions import Wetlands, PettingZoo, SnakePit

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow", 563154874)
lady_goat = Goat("The G.O.A.T", "domestic goat", "morning", "cracked corn", 563175869)
donkey = Donkey("Dwayne", "domestic donkey", "midday", "hay and oats", 896471258)
little_pony = Pony("Princess", "domestic pony", "afternoon", "hay and oats", 846325987)
silver_bullet = Alpaca("Silver Bullet", "domestic alpaca", "afternoon", "mixed fruit and nuts", 876325984)
copperhead = CopperHead("Dan", "venomous snake", "dead mice", 874526986)
king_cobra = KingCobra("Slytherin", "venomous snake", "dead mice", 235486921)
mallard = Mallard("Wendy", "duck", "bread crumbs", 864236598)
rat_snake = RatSnake("Basil", "non-venomous snake", "dead mice", 896542365)
anaconda = GiantAnaconda("Jafaar", "boa constrictor", "medium sized bird", 364785698)
cottonmouth = Cottonmouth("Medusa", "venomous snake", "dead lizzard", 903652547)
goldfish = GoldFish("Milo", "fish", "dried worms", 869547125)
stonefish = StoneFish("Fluffy", "venomous fish", "5 minnows", 896473265)
octopus = BlueRingedOctopus("Atlantis", "octopus", "small crabs and shrimp", 258946257)
jellyfish = BoxJellyfish("Angel", "jellyfish", "worms and shrimp", 789654123)


varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
slither_inn = SnakePit("Slither Inn", "slithering and creepy critters to gaze at")
critter_cove = Wetlands("Critter Cove", "water loving critters in the wetlands")

varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(lady_goat)
varmint_village.add_animal(donkey)
varmint_village.add_animal(little_pony)
varmint_village.add_animal(silver_bullet)
slither_inn.add_animal(copperhead)
slither_inn.add_animal(king_cobra)
slither_inn.add_animal(rat_snake)
slither_inn.add_animal(anaconda)
slither_inn.add_animal(cottonmouth)
critter_cove.add_animal(goldfish)
critter_cove.add_animal(stonefish)
critter_cove.add_animal(mallard)
critter_cove.add_animal(octopus)
critter_cove.add_animal(jellyfish)

# print(varmint_village.last_critter_added)
# print(slither_inn.last_critter_added)
for animal in critter_cove.animals:
    print(animal)

critter_cove.remove_animal(jellyfish)
print("-------------")
for animal in critter_cove.animals:
    print(animal)