def multiples():
    L=[8,24,48,2,16]
    print(L)
    mult3=0
    for n in L:
        if n % 3== 0:
            mult3+=1
        print("Le nombre de multiples de 3 dans la liste est :",mult3)
multiples()