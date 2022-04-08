from choipeaux_magique_pourlapartie2 import *
from browser import document as doc, html
import csv
from random import randint

k=7
doc <= html.H4(html.IMG(src='refresh.png', id='refresh', value="Rafraîchir la page", onClick="history.go(0)"))
doc <= html.H1("Bienvenue sur notre quesionnaire", id='welcome')
doc <= html.IMG(src="choipeaux.png", id="img")
doc <= html.P(html.BUTTON('COMMENCER', id= 'start'))
doc <= html.H2(html.IMG(src='maisons_poudlard.png', id='maisons'))
doc <= html.I(html.B(html.H3("Appuyer sur COMMENCER pour lancer le questionnaire", id='txt_dbt')))

with open("Questions.csv", mode='r', encoding='utf-8') as g:
    reader = csv.DictReader(g, delimiter=',')
    questions = [{key: value for key, value in element.items()} for element in reader]
new_dico = {}

liste_valeurs_perso = [0, 0, 0, 0]
liste_ajustement = [0, 0, 0, 0]
for question in questions:
    iteme = question.items()

    for (cle, valeur) in iteme:
        couple = valeur.split("/")
        dico = {}
        """
        les lignes suivante permettent de créer le dictionnaire des questions et réponses sous la forme:
        {"question1":{"reponse1": [1, 2, 3]}, "reponse2": [1, 2, 3]}...
        "question2":{"reponse1": [1, 2, 3]}, "reponse2": [1, 2, 3]}...} 
        le "+3" permet de rendre toutes les valeurs d'ajustement positifs ou nul pour
        rendre l'ajustement plus facile.
        """
        liste_valeur = [int(i) + 3 for i in couple[1].split(',')]
        liste_ajustement = [liste_ajustement[i] + liste_valeur[i] for i in range(4)]

        dico[couple[0]] = liste_valeur
        if cle not in new_dico.keys():
            new_dico[cle] = dico

        else :
            new_dico[cle].update(dico)



liste_qst = list(new_dico.keys())
liste_ajustement = [round(v/3) for v in liste_ajustement] #on divise par le nombre de réponse  
"""
Cette liste correspond aux moyennes représentatives des différentes qualité
des personnages d'Harry Potter.
"""
liste_moyenne = [6.43, 5.84, 6.66, 7.41] # valeur provenant du fichier ajustement.py
print(liste_valeurs_perso)
liste_ajustement = [liste_moyenne[i]-liste_ajustement[i] for i in range(4)]
print(liste_ajustement)

nm_qstn = 0  # le numéro de la question a la quelle on est rendue
def click(event):
    '''
    Cette procédure permet après le clique d'une des réponses la mise
    à jour du profil et le changement de texte des questions et des 
    réponses via la fonction "affichage_question".
    '''
    global nb_qstn  
    global nm_qstn
    global liste_valeurs_perso
    nm_qstn += 1 

    if nm_qstn < len(liste_qst):
        text_btn = event.target.text        
        affichage_question(new_dico, liste_qst, nm_qstn)
        ajustement = new_dico[liste_qst[nm_qstn-1]][text_btn]
        liste_valeurs_perso = [ajustement[i] + liste_valeurs_perso[i] for i in range(4)]
        
    else:
        doc['result'].style.display ='inline'
        doc['rep1'].style.display ='none'
        doc['rep2'].style.display ='none'
        doc['rep3'].style.display ='none'
        doc['texte_qst'].style.display ='none'

click_on_result = 1
def resultat(event):
    '''
    Cette fonction permet de finaliser le profil et d'afficher la maison
    et les k + proche voisins 
    '''
    global click_on_result
    global liste_valeurs_perso
    if click_on_result == 1:
        print("liste_ajustemnt =  ", liste_ajustement)
        print("liste_valeurs_perso1 = ", liste_valeurs_perso)
        liste_valeurs_perso = [liste_valeurs_perso[i]+liste_ajustement[i] for i in range(4)]
        liste_valeurs_perso = [a if a < 10 else 10 for a in liste_valeurs_perso]
        liste_valeurs_perso = [a if 0 < a  else 0 for a in liste_valeurs_perso]
        print("liste_valeurs_perso = ", liste_valeurs_perso)
        user = {'Courage':liste_valeurs_perso[0]   , 'Ambition': 10 + liste_valeurs_perso[1], 'Intelligence': 10 + liste_valeurs_perso[2], 'Good': 10 + liste_valeurs_perso[3]}
        doc <= html.H3(f"La maison attribué à cet élève est {maison(poudlard_characters, user, k)}")
        doc <= html.B(f'Vos {k} voisins sont: ')
        
        if maison(poudlard_characters, user, k=7) == 'Gryffindor':
            for dico in kkpv(poudlard_characters, user, k):
                house = dico['House']
                nom = dico['Name']
                doc <= html.P(f"L'élève {nom} de la maison {house}",id ='voisins_grif')  
            doc <= html.H2(html.IMG(src='griffondor.png', id='user_house'))

        elif maison(poudlard_characters, user, k=7) == 'Ravenclaw':
            for dico in kkpv(poudlard_characters, user, k):
                house = dico['House']
                nom = dico['Name']
                doc <= html.P(f"L'élève {nom} de la maison {house}",id ='voisins_serd')
            doc <= html.H2(html.IMG(src='serdaigle.png', id='user_house'))

        elif maison(poudlard_characters, user, k=7) == 'Hufflepuff':
            for dico in kkpv(poudlard_characters, user, k):
                house = dico['House']
                nom = dico['Name']
                doc <= html.P(f"L'élève {nom} de la maison {house}",id ='voisins_pouf')
            doc <= html.H2(html.IMG(src='poufsouffle.png', id='user_house'))

        elif maison(poudlard_characters, user, k=7) == 'Slytherin':
            for dico in kkpv(poudlard_characters, user, k):
                house = dico['House']
                nom = dico['Name']
                doc <= html.P(f"L'élève {nom} de la maison {house}",id ='voisins_serp')
            doc <= html.H2(html.IMG(src='serpentard.png', id='user_house'))
            
    click_on_result +=1

def start(event):
    '''
    Cette fonction sert à afficher seulement notre page d'accueil 
    '''
    doc['start'].style.display = 'none'
    doc['txt_dbt'].style.display = 'none'
    doc['maisons'].style.display = 'none'
    doc['welcome'].style.display = 'none'


    doc['texte_qst'].style.display ='inline'
    doc['rep1'].style.display ='inline'
    doc['rep2'].style.display ='inline'
    doc['rep3'].style.display ='inline'

doc <= html.B('Question', id="texte_qst")


doc <= html.P(html.BUTTON('Reponse', id= "rep1", value=0))
doc <= html.P(html.BUTTON('Reponse', id= "rep2", value=1))
doc <= html.P(html.BUTTON('Reponse', id= "rep3", value=2))

doc <= html.BUTTON('Résultat', id= "result")

doc['texte_qst'].style.display ='none'
doc['result'].style.display ='none'
doc['rep1'].style.display ='none'
doc['rep2'].style.display ='none'
doc['rep3'].style.display ='none'

doc['rep1'].bind('click', click)
doc['rep2'].bind('click', click)
doc['rep3'].bind('click', click)
doc['start'].bind('click', start)
doc['result'].bind('click', resultat)

def affichage_question(dico_qtsn ,liste_qstn, n_qstn):
    '''
    Paramètre: dico_qstn(dictionnaire), liste_qstn(liste), n_qstn(entier)
    Cette procédure permet de changer le contenu des questions
    et des réponses.
    '''
    question = liste_qstn[n_qstn]
    liste_reponse = list(dico_qtsn[question].keys())
    doc["texte_qst"].textContent = question
    doc["rep1"].textContent = liste_reponse[0]
    doc["rep2"].textContent = liste_reponse[1]
    doc["rep3"].textContent = liste_reponse[2]

affichage_question(new_dico, liste_qst, nm_qstn)

nb_test = 100
ça_fonctionne = 0
for _ in range(nb_test):
    train_set = [poudlard_characters[randint(i, len(poudlard_characters)-1)] for i in range(int(len(poudlard_characters)*0.8))]
    test_set = [poudlard_characters[randint(i, len(poudlard_characters)-1)] for i in range(int(len(poudlard_characters)*0.2))]
    for eleve in test_set:
        if maison(train_set, eleve, k) == eleve['House']:
            ça_fonctionne += 1
#print(f"Le pourcentage de réussite du programme est de {round(ça_fonctionne / len(test_set), 2)}% avec {k} voisins")