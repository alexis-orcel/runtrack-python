def print_produce(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "été":
            print("poire, fraise, cassis")
    elif type == "légume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "été":
            print("artichaut, aubergine, navet")
print_produce("fruits", "hiver")
print_produce("fruits", "été")
print_produce("légume", "hiver")
print_produce("légume", "été")
