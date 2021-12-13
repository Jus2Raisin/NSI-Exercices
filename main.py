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

