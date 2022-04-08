import csv

with open("Characters.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    characters = [{key: value for key, value in element.items()} for element in reader]

with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as h:
    reader = csv.DictReader(h, delimiter=';')
    caracteristiques = [{key: value for key, value in element.items()} for element in reader]

poudlard_characters = []

for poudlard_character in caracteristiques:
    for i in characters:
        if poudlard_character['Name'] == i['Name']:
            poudlard_character.update(i)
            poudlard_characters.append(poudlard_character)

Hufflepuff=0
Gryffindor=0
Ravenclaw=0
Slytherin=0

liste_qualite = ['Courage', 'Ambition', 'Intelligence', 'Good']


for dico in poudlard_characters:
    if dico['House']== 'Gryffindor' :
        Gryffindor += 1
    elif dico['House']== 'Hufflepuff':
        Hufflepuff += 1
    elif dico['House']=='Ravenclaw':
        Ravenclaw+= 1
    elif dico['House']== 'Slytherin':
        Slytherin+=1

print(Hufflepuff)
print(Gryffindor)
print(Ravenclaw)
print(Ravenclaw)


list_huffle = []
list_gryffin=[]
list_Raven=[]
list_slyth=[]

maison_min = min([Hufflepuff, Gryffindor, Ravenclaw, Ravenclaw])

for dico in poudlard_characters:
    if dico['House']== 'Gryffindor' and len(list_gryffin) < 13: 
        list_gryffin.append(dico)
    elif dico['House']== 'Hufflepuff' and len(list_huffle) < 13:
        list_huffle.append(dico)
    elif dico['House']=='Ravenclaw' and len(list_Raven) < 13:
        list_Raven.append(dico)
    elif dico['House']== 'Slytherin' and len(list_slyth) < 13:
        list_slyth.append(dico)


liste_reparti = list_huffle + list_gryffin + list_Raven + list_slyth
listes_valeurs = []

for dico in liste_reparti:
     listes_valeurs.append([dico[qualite] for qualite in liste_qualite])
print(listes_valeurs)

total_valeur = [0, 0, 0, 0]

for valeur in listes_valeurs:
    total_valeur = [total_valeur[i]+int(valeur[i]) for i in range(4)]

total_valeur = [total_valeur[i]/52 for i in range(4)]
print(total_valeur)
