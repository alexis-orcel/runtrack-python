s = "abcdefghijklmnopqrstuvwxyz" * 10

# On calcule la taille de la pyramide en trouvant la première puissance de 2 qui est
# supérieure à la longueur de la chaîne
n = 1
while n ** 2 < len(s):
    n += 1

# On imprime la pyramide en parcourant la chaîne s caractère par caractère et en
# ajoutant des espaces pour aligner les caractères sur la pyramide
for i in range(n):
    print(" " * (n - i - 1) + s[i::n])