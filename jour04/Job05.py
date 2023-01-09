def remplacer_case(L, i):
    L[i] = L[i-1] + L[i+1]

L = [7, 11, 42, 39, 2]

print(L[1])

remplacer_case(L, 3)

print(L[-1])