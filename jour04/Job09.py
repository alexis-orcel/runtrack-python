def max_min(liste):
    maxi = liste[0]
    mini = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > maxi:
            maxi = liste[i]
        if liste[i] < mini:
            mini = liste[i]
    return maxi, mini

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
maximum, minimum = max_min(L)
print("Le maximum est", maximum)
print("Le minimum est", minimum)
