def arrondir_notes(notes):
  notes_arrondies = []
  for note in notes:
    if note >= 40:
      if note % 5 >= 3:
        note = note + (5 - note % 5)
      notes_arrondies.append(note)
    else:
      notes_arrondies.append(note)
  return notes_arrondies

notes = [82, 83, 84, 85, 86]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)  # Imprime [82, 85, 85, 85, 85]
