def chiffrement_cesar(message, decalage):
  resultat = ""
  for lettre in message:
    if lettre.isalpha():
      num_lettre = ord(lettre)
      num_lettre += decalage
      if lettre.islower():
        if num_lettre > ord('z'):
          num_lettre -= 26
        elif num_lettre < ord('a'):
          num_lettre += 26
      else:
        if num_lettre > ord('Z'):
          num_lettre -= 26
        elif num_lettre < ord('A'):
          num_lettre += 26
      resultat += chr(num_lettre)
    else:
      resultat += lettre
  return resultat

message_chiffre = chiffrement_cesar("abc", 3)
print(message_chiffre)  # Imprime "def"

message_dechiffre = chiffrement_cesar(message_chiffre, -3)
print(message_dechiffre)  # Imprime "abc"
