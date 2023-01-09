def compte_multiples_de_3(L):

    compte = 0

    for element in L:

        if element % 3 == 0:
            compte += 1

    return compte

L = [8, 24, 48, 2, 16]
resultat = compte_multiples_de_3(L)
print(f"Le nombre de multiples de 3 dans la liste est {resultat}.")
