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

with open('animals.txt', 'r') as f:
    animals = f.readlines()

with open('animal_parts.txt', 'r') as f:
    animal_parts = f.readlines()

with open('inf_diseases.txt', 'r') as f:
    inf_diseases = f.readlines()

with open('viruses_filtered.txt', 'r') as f:
    viruses = f.readlines()

with open('plants.txt', 'r') as f:
    plants = f.readlines()

with open('plant_parts.txt', 'r') as f:
    plant_parts = f.readlines()

with open('part_modifiers.txt', 'r') as f:
    part_modifiers = f.readlines()

with open('liquids.txt', 'r') as f:
    liquids = f.readlines()

with open('neuro.txt', 'r') as f:
    neuro = f.readlines()

with open('disorders.txt', 'r') as f:
    disorders = f.readlines()

sickness = random.choice(inf_diseases + viruses + neuro + disorders)[0:-1]
ing_list = []
for i in range(random.randint(1,6)):
    ing = str(random.randint(1,6)) + " parts "
    ing += random.choice(part_modifiers)[0:-1]
    if random.randint(0,1) > 0:
        ing += " " + random.choice(animal_parts)[0:-1]
        ing += " of the " + random.choice(animals)[0:-1]
    else:
        ing += " " + random.choice(plant_parts)[0:-1]
        ing += " of the " + random.choice(plants)[0:-1]
    ing_list.append(ing)
print "To cure " + sickness + ", combine and ingest the following:\n" \
    + str(random.randint(2,10)) + " parts " + random.choice(liquids) \
    + '\n'.join(ing_list)
