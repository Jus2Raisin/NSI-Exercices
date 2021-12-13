# -*- coding: utf-8 -*-
"""
Created on Wed Dec 8 09:35:23 2021

@author: sohan

Ecrire un programme qui prend en entrée une chaine de caractères comprenant une liste de 3 champs séparés par des caractères ';' (un numéro d'etudiant, un nom et un prenom) 
et retourne un dictionnaire dont les clés sont les numéros d'étudiants et les valeurs sont, 
pour chaque numéro d'étudiant, une chaine correspodant à la concaténation des prénom et nom de la personne. 
On pourra tester la fonction avec la chaîne suivante : chaine = "2136;BESNIER;JEAN 2135;DUPOND;MARC 2146;DURAND;JULIE"

"""
chaine = "2136;BESNIER;JEAN 2135;DUPOND;MARC 2146;DURAND;JULIE"
etudiants = list()
dictionnaire = dict()
x=0
for i in range(len(chaine)):
    if chaine[i] == " ":
        etudiants.append(chaine[x:i])
        x=i+1
    if i == len(chaine)-1:
        etudiants.append(chaine[x:])

for i in range(len(etudiants)):
    for k in range(5, len(etudiants[i])):
        if etudiants[i][k] == ";":
            dictionnaire[etudiants[i][:4]] = etudiants[i][k+1:] + " " + etudiants[i][5:k]

print(dictionnaire)
print()
for key in dictionnaire.keys():
    print(dictionnaire[key], "a pour numéro le n°"+str(key))

