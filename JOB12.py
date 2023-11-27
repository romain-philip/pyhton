def croissant(liste):
    L=[]
    while liste:
       mini=min(liste)
       liste.remove(mini)
       L.append(mini)
    return L
print (croissant([2,1,5,3,4]))