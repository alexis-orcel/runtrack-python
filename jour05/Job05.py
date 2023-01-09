def distance_marches(marches, hauteur):
  distance = (marches * hauteur * 2) / 100
  semaine = distance * 5 * 7
  print("Pour", marches, "marches de", hauteur, "cm, le gardien parcourt", semaine, "m par semaine.")

distance_marches(100, 20)  # Imprime "Pour 100 marches de 20 cm, le gardien parcourt 140.0 m par semaine."
