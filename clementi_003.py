import math

# Chiedi all'utente di inserire il raggio
raggio = float(input("Inserisci il raggio del cerchio: "))

# Calcola la circonferenza del cerchio
circonferenza = 2 * math.pi * raggio

# Calcola l'area del cerchio
area = math.pi * (raggio ** 2)

# Visualizza la circonferenza e l'area del cerchio
print("La circonferenza del cerchio è:", circonferenza)
print("L'area del cerchio è:", area)