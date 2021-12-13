# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:35:23 2021

@author: sohan

Ecrire un programme qui à partir d'une chaine de caractère saisie en lettres minuscules au clavier, place dans un dictionnaire les lettres présentes dans la chaine et leur nombre d'occurences respectif.

"""
chaine = input("Entrez une chaine : ")
Dictionnaire = dict()
x = 0
for i in range(len(chaine) - 1, -1, -1):
    Dictionnaire[chaine[i]] = 0
    for j in range(len(chaine)):
        if chaine[j] == chaine[i]:
            x = Dictionnaire[chaine[i]] + 1
            Dictionnaire[chaine[i]] = x
print(Dictionnaire)
