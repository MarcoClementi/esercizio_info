#Chiesti all’utente 5 voti in input dire quanti di questi sono sufficienti su quelli 
# considerati validi. I voti sono considerati validi se compresi tra 1 e 10.
voto_1 = int(input("Inserisci il voto: "))
voto_2 = int(input("Inserisci il voto: "))
voto_3 = int(input("Inserisci il voto: "))
voto_4 = int(input("Inserisci il voto: "))
voto_5 = int(input("Inserisci il voto: "))

valid_range = range(1, 11)  # Valid range for votes is from 1 to 10

if voto_1 in valid_range:
    print("Il numero è valido.")
else:
    print("Il numero non è valido.")

if voto_2 in valid_range:
    print("Il numero è valido.")
else:
    print("Il numero non è valido.")

if voto_3 in valid_range:
    print("Il numero è valido.")
else:
    print("Il numero non è valido.")

if voto_4 in valid_range:
    print("Il numero è valido.")
else:
    print("Il numero non è valido.")

if voto_5 in valid_range:
    print("Il numero è valido.")
else:
    print("Il numero non è valido.")
