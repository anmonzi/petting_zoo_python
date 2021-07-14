from petting_area import Llama, Goat, Donkey, Pony, Alpaca
from glass_tank import Copperhead, KingCobra, RatSnake, GiantAnaconda, Cottonmouth
from pond import Goldfish, Stonefish, Mallard, BlueRingedOctopus, BoxJellyfish
from attractions import PettingZoo, SnakePit, Wetlands


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow", 563154874)
lady_goat = Goat("The G.O.A.T", "domestic goat", "morning", "cracked corn")
donkey = Donkey("Dwayne", "domestic donkey", "midday", "hay and oats")
little_pony = Pony("Princess", "domestic pony", "afternoon", "hay and oats")
silver_bullet = Alpaca("Silver Bullet", "domestic alpaca", "afternoon", "mixed fruit and nuts")
copperhead = Copperhead("Dan", "venomous snake", "dead mice")
king_cobra = KingCobra("Slytherin", "venomous snake", "dead mice")
rat_snake = RatSnake("Basil", "non-venomous snake", "dead mice")
anaconda = GiantAnaconda("Jafaar", "boa constrictor", "medium sized bird")
cottonmouth = Cottonmouth("Medusa", "venomous snake", "dead lizzard")
goldfish = Goldfish("Milo", "fish", "dried worms")
stonefish = Stonefish("Fluffy", "venomous fish", "5 minnows")
mallard = Mallard("Ricky", "bird", "seeds and roots")
octopus = BlueRingedOctopus("Atlantis", "octopus", "small crabs and shrimp")
jellyfish = BoxJellyfish("Angel", "jellyfish", "worms and shrimp")


varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
slither_inn = SnakePit("Slither Inn", "slithering and creepy critters to gaze at")
critter_cove = Wetlands("Critter Cove", "water loving critters in the wetlands")

varmint_village.animals.append(miss_fuzz)
varmint_village.animals.append(lady_goat)
varmint_village.animals.append(donkey)
varmint_village.animals.append(little_pony)
varmint_village.animals.append(silver_bullet)
slither_inn.animals.append(copperhead)
slither_inn.animals.append(king_cobra)
slither_inn.animals.append(rat_snake)
slither_inn.animals.append(anaconda)
slither_inn.animals.append(cottonmouth)
critter_cove.animals.append(goldfish)
critter_cove.animals.append(stonefish)
critter_cove.animals.append(mallard)
critter_cove.animals.append(octopus)
critter_cove.animals.append(jellyfish)

print(varmint_village.last_critter_added)
print(slither_inn.last_critter_added)
print(critter_cove.last_critter_added)