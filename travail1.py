import FonctionsImageListe as FI


def createPicture(liste, path):
    FI.ExportImageListeListeTuple(liste, path)
    FI.AffichageImage(path)
    print("L'image " + path[:len(path) - 4] + " a été crée !")


#
# Début de la Partie III
#

imagePATH = str("Lena.png")
FI.AffichageImage(imagePATH)
List = FI.ImportImageListeListeTuple(imagePATH)

# lena_niv_gris
for i in range(len(List)):
    for j in range(len(List[i])):
        x = (List[i][j][0] + List[i][j][1] + List[i][j][2]) // 3
        List[i][j] = (x, x, x)
createPicture(List, "lena_niv_gris.png")

# lena_gris_negatif
List = FI.ImportImageListeListeTuple(imagePATH)
for i in range(len(List)):
    for j in range(len(List[i])):
        x = (List[i][j][0] + List[i][j][1] + List[i][j][2]) // 3  #
        List[i][j] = (255 - x, 255 - x, 255 - x)
createPicture(List, "lena_neg_gris.png")

# lena_bleu
List = FI.ImportImageListeListeTuple(imagePATH)
for i in range(len(List)):
    for j in range(len(List[i])):
        List[i][j] = (0, 0, List[i][j][2])
createPicture(List, "lena_B.png")

# lena_vert
List = FI.ImportImageListeListeTuple(imagePATH)
for i in range(len(List)):
    for j in range(len(List[i])):
        List[i][j] = (0, List[i][j][1], 0)
createPicture(List, "lena_V.png")

# lena_rouge
List = FI.ImportImageListeListeTuple(imagePATH)
for i in range(len(List)):
    for j in range(len(List[i])):
        List[i][j] = (List[i][j][0], 0, 0)
createPicture(List, "lena_R.png")

# lena_negatif_color
List = FI.ImportImageListeListeTuple(imagePATH)
for i in range(len(List)):
    for j in range(len(List[i])):
        List[i][j] = (255 - List[i][j][0], 255 - List[i][j][1], 255 - List[i][j][2])
createPicture(List, "lena_neg_coul.png")

# lena_noir_&_blanc
List = FI.ImportImageListeListeTuple(imagePATH)
for i in range(len(List)):
    for j in range(len(List[i])):
        X = 0 if (List[i][j][0] + List[i][j][1] + List[i][j][2]) // 3 < 128 else 255
        List[i][j] = (X, X, X)
createPicture(List, "lena_n_et_b.png")
