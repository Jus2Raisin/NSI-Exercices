import FonctionsImageListe as FI


def createPicture(liste, path):
    FI.ExportImageListeListeTuple(liste, path)
    FI.AffichageImage(path)
    print("L'image " + path[:len(path) - 4] + " a été crée !")

LenaList = FI.ImportImageListeListeTuple(str("Lena.png"))
PangolinList = FI.ImportImageListeListeTuple(str("Pangolin.png"))
a = float(input("Entrez le coefficient de dominance de l'image: "))

for i in range(len(LenaList)):
    for j in range(len(LenaList[i])):
        LenaList[i][j] = (int(a*LenaList[i][j][0]) + int((1-a)*PangolinList[i][j][0]), int(a*LenaList[i][j][1]) + int((1-a)*PangolinList[i][j][1]), int(a*LenaList[i][j][2]) + int((1-a)*PangolinList[i][j][2]))
createPicture(LenaList, "Lena_pangolin.png")

