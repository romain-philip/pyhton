def my_long_word(n, phrase):
    mots = []
    mot = ""
    phrase += " "  
    
    for caractere in phrase:
        if caractere != " ":
            mot += caractere
        else:
            count = 0
            for _ in mot:
                count += 1
            if count > n:
                mots.append(mot)
            mot = ""
    return " ".join(mots)
chiffre = 3
chaine = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(chiffre, chaine)
print("Output:", resultat)