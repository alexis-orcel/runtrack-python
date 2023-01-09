def est_premier(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

for x in range(2, 1001):
  if est_premier(x):
    print(x)