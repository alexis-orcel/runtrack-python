def augmenter_liste(L):
    for i in range(len(L)):
        L[i] += 1
    return L

L = [7, 11, 42, 39, 2]
print(augmenter_liste(L))
