def dessiner_rectangle(largeur, hauteur):
  print("+" + "-" * largeur + "+")
  for i in range(hauteur):
    print("|" + " " * largeur + "|")
  print("+" + "-" * largeur + "+")

dessiner_rectangle(10, 3)
