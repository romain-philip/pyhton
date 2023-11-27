def produits():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    print(L)
    valeurs_dans_intervalle = [valeur for valeur in L if 25 <= valeur <= 90]
    produit = 1
    for valeur in valeurs_dans_intervalle:
     produit *= valeur
    print("Le produit des valeurs dans l'intervalle [25, 90] est :", produit) 
produits()  