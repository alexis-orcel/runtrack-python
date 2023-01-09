def somme_valeurs_paires(L):
    somme = 0
    for element in L:
        if element % 2 == 0:
            somme += element
    return somme

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
resultat = somme_valeurs_paires(L)
print(f"La somme des valeurs paires de la liste est {resultat}.")
