def echange_premiere_et_derniere(L):

    L[0], L[-1] = L[-1], L[0]

L = [1, 2, 3, 4, 5]

echange_premiere_et_derniere(L)

print(L)
