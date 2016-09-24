import random

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

animals = []
animal_parts = []
inf_diseases = []
viruses = []
plants = []
plant_parts = []
part_modifiers = []
liquids = []
neuro = []
disorders = []
skin_disorders = []
minerals = []
mineral_modifiers = []
rivers = []
seas = []
springs = []
greek_mythos = []

with open('lists/animals.txt', 'r') as f:
    animals = f.readlines()

with open('lists/animal_parts.txt', 'r') as f:
    animal_parts = f.readlines()

with open('lists/inf_diseases.txt', 'r') as f:
    inf_diseases = f.readlines()

with open('lists/viruses_filtered.txt', 'r') as f:
    viruses = f.readlines()

with open('lists/plants.txt', 'r') as f:
    plants = f.readlines()

with open('lists/plant_parts.txt', 'r') as f:
    plant_parts = f.readlines()

with open('lists/part_modifiers.txt', 'r') as f:
    part_modifiers = f.readlines()

with open('lists/liquids.txt', 'r') as f:
    liquids = f.readlines()

with open('lists/neuro.txt', 'r') as f:
    neuro = f.readlines()

with open('lists/disorders.txt', 'r') as f:
    disorders = f.readlines()

with open('lists/skin_disorders.txt', 'r') as f:
    skin_disorders = f.readlines()

with open('lists/minerals.txt', 'r') as f:
    minerals = f.readlines()

with open('lists/mineral_modifiers.txt', 'r') as f:
    mineral_modifiers = f.readlines()

with open('lists/rivers.txt', 'r') as f:
    rivers = f.readlines()

with open('lists/seas.txt', 'r') as f:
    seas = f.readlines()

with open('lists/springs.txt', 'r') as f:
    springs = f.readlines()

with open('lists/greek_mythos.txt', 'r') as f:
    greek_mythos = f.readlines()

def get_disorder():
    return random.choice(inf_diseases + viruses + neuro + disorders)[0:-1]

def get_skin_disorder():
    return random.choice(skin_disorders)[0:-1]

def get_animal_ingredient():
    ing = random.choice(part_modifiers)[0:-1]
    ing += " " + random.choice(animal_parts)[0:-1]
    ing += " of the " + random.choice(animals)[0:-1]
    return ing

def get_plant_ingredient():
    ing = random.choice(part_modifiers)[0:-1]
    ing += " " + random.choice(plant_parts)[0:-1]
    ing += " of the " + random.choice(plants)[0:-1]
    return ing

def get_solvent_ingredient():
    # kept the "parts" part because different numbers
    return str(random.randint(2,10)) + " parts " + random.choice(liquids)[0:-1]

def get_mineral_ingredient():
    ing = random.choice(mineral_modifiers)[0:-1]
    ing += " " + random.choice(minerals)[0:-1]
    return ing

def get_random_ingredient():
    ing = str(random.randint(1,6)) + " parts "
    ra = random.randint(0, 12)
    if ra > 9:
        ing += get_animal_ingredient()
    elif ra > 6:
        ing += get_plant_ingredient()
    elif ra > 3:
        ing += get_mineral_ingredient()
    elif ra >1:
        # get_solvent does its own "parts" generation, so just assign, don't append
        ing = get_solvent_ingredient()
    else:
        ing = get_water_ingredient()
    return ing

def get_water_ingredient():
    ing = str(random.randint(2,10)) + " parts water from the "
    ra = random.randint(0,2)
    if ra == 0:
        ing += "River " + random.choice(rivers)[0:-1]
    elif ra == 1:
        ing += random.choice(seas)[0:-1]
    else:
        ing += random.choice(springs)[0:-1] + " Spring"
    return ing

def get_greek_mythos():
    return random.choice(greek_mythos)[0:-1]

def create_recipe():
    ing_list = [get_water_ingredient()]
    for i in range(random.randint(1,5)):
        ing_list.append(get_random_ingredient())
    return '\n'.join(ing_list)

def get_prayer():
    return "Pray to " + get_greek_mythos() + "."

def create_cure():
    malady = "To cure "
    prayer = get_prayer()
    prayer += "\nThen "
    if random.randint(0,1):
        malady += get_disorder() + ":\n" + prayer + "combine and ingest the following:"
    else:
        malady += get_skin_disorder() + ":\n" + prayer + "apply a poultice composed of the following:"
    malady += '\n' + create_recipe()
    print malady

if __name__ == "__main__":
    create_cure()
