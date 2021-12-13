# -*- coding: utf-8 -*-
"""
Created on Tues Dec 13 22:24:22 2021

@author: sohan

Ecrire un programme qui prend en entrée un dictionnaire associant à un élève une liste de notes et
qui affiche le (ou les) élève(s) qui a (ont) la moyenne la plus élevée et la moyenne correspondante.
On pourra utiliser le dictionnaire suivant pour tester le programme :
notes = {"Tom": [8, 10, 12], "Mila": [10, 9], "Alex": [4], "Lina": [12, 10, 8]}
Indice: créer un 2eme dictionnaire notes2 qui contient les noms des élèves associés à leur moyenne.

"""
notes = {"Tom": [8, 10, 12], "Mila": [10, 9], "Alex": [4], "Lina": [12, 10, 8]}
notes2 = {}
for key in notes.keys():
    somme = 0
    for i in range(len(notes[key])):
        somme += notes[key][i]
        notes2[key] = (somme/len(notes[key]))
maximum = 0
for key in notes2.keys():
    if notes2[key] > maximum:
        maximum = notes2[key]
for key in notes2.keys():
    if notes2[key] == maximum:
        print(key, "a la moyenne la plus élévé avec", maximum, "de moyenne")

