liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
compteur = 0
for _ in liste:
    compteur += 1
arrondis = []
for i in range(compteur):
    arrondi = int(liste[i] + 0.5) if liste[i] >= 0 else int(liste[i] - 0.5)
    arrondis.append(arrondi)
index = 0
trie_effectue = False
while not trie_effectue:
    trie_effectue = True
    index += 1
    for i in range(compteur - index):
        if arrondis[i] > arrondis[i + 1]:
            arrondis[i], arrondis[i + 1] = arrondis[i + 1], arrondis[i]
            liste[i], liste[i + 1] = liste[i + 1], liste[i]
            trie_effectue = False
print("Liste initiale arrondie et triée : ", liste)