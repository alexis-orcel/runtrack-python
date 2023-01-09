def print_diagonal_carpet(n):
  for i in range(n+1):
    for j in range(n+1):
      if i == j:
        print('X', end=' ')
      else:
        print('-', end=' ')
    print()

print_diagonal_carpet(10)
