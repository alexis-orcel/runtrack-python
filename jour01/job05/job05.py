import string

def reverseAlphabet():
  alphabet = list(string.ascii_lowercase)
  alphabet.reverse()
  return alphabet

print(reverseAlphabet())