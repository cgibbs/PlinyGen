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
    ra = random.randint(0,4)
    if ra == 0:
        ing += get_animal_ingredient()
    elif ra == 1:
        ing += get_plant_ingredient()
    elif ra == 2:
        # get_solvent does its own "parts" generation, so just assign, don't append
        ing = get_solvent_ingredient()
    else:
        ing += get_mineral_ingredient()
    return ing

def create_recipe():
    ing_list = [get_solvent_ingredient()]
    malady = "To cure "
    if random.randint(0,1):
        malady += get_disorder() + ", combine and ingest the following:\n"
    else:
        malady += get_skin_disorder() + ", apply a poultice composed of the following:\n"
    for i in range(random.randint(1,6)):
        ing_list.append(get_random_ingredient())
    print malady + '\n'.join(ing_list)

if __name__ == "__main__":
    create_recipe()
