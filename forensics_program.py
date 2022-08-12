import json

characteristics_culprit = {}
characteristics_counter = 0

with open("dna_characteristics.json", "r") as dna_characteristics_file:
    dna_characteristics = json.loads(dna_characteristics_file.read())
with open("dna.txt", "r") as dna_culprit_file:
    dna_culprit = dna_culprit_file.read()
with open("suspects.json", "r") as suspects_file:
    characteristics_suspects = json.loads(suspects_file.read())

for characteristics_key, characteristics_value_dict in dna_characteristics.items():
    for property, dna in characteristics_value_dict.items():
        if dna_culprit.find(dna) != -1:
            characteristics_culprit[characteristics_key] = property

for person, characteristics in characteristics_suspects.items():
    for characteristic, property in characteristics.items():
        if characteristics_culprit[characteristic] != property:
             characteristics_counter = 0
             break
        else:
            characteristics_counter += 1

    if characteristics_counter == 5:
        print("The thief is... ")
        input("--- pause for suspense (press enter) ---")
        print(person.upper() + "! :O")
        quit()

