def ajout_fruit_a_index():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.insert(2, "Mangue")
    return fruits

fruits = ajout_fruit_a_index()
print(fruits)
