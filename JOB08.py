def somme_valeurs_paires():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    print(L)
    somme = 0
    for nombre in L:
        if nombre % 2 == 0: 
            somme += nombre  
    return somme
resultat = somme_valeurs_paires()
print("La somme des valeurs paires de la liste est :", resultat)