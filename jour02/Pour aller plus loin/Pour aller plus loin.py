def classify_triangle(a, b, c):
    # Vérifier s'il est possible de construire un triangle avec les longueurs données
    if a + b > c and a + c > b and b + c > a:
        # Vérifier si le triangle est rectangle
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Triangle rectangle")
        # Vérifier si le triangle est isocèle
        elif a == b or a == c or b == c:
            print("Triangle isocèle")
        # Vérifier si le triangle est équilatéral
        elif a == b and b == c:
            print("Triangle équilatéral")
        # Si le triangle n'est ni rectangle, ni isocèle, ni équilatéral, il est quelconque
        else:
            print("Triangle quelconque")
    # Si les longueurs données ne permettent pas de construire un triangle, afficher un message d'erreur
    else:
        print("Impossible de construire un triangle avec les longueurs données")
classify_triangle(2, 4, 6)
classify_triangle(5, 5, 5)
classify_triangle(8, 8, 9)
classify_triangle(1, 2, 3)