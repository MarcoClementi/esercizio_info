n = int(input("Inserisci il numero di pasticcini: "))


q1 = n // 5


n = n - (q1 * 5)

q2 = n // 3


n = n - (q2 * 3)


q3 = n


print("Numero di scatole da 5 pezzi:", q1)
print("Numero di scatole da 3 pezzi:", q2)
print("Numero di scatole da 1 pezzo:", q3)