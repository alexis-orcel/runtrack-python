def produit_intervalle(L, a, b):
    produit = 1
    for x in L:
        if x >= a and x <= b:
            produit *= x
    return produit

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(produit_intervalle(L, 25, 90))

