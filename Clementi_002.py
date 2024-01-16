#Chiesto all’utente un anno in input controllare la validità dell’input (0<anno<2100) e
# dire se esso è bisestile o no.
# A tal fine, implementare il seguente algoritmo:
# Un anno è bisestile se esso è divisibile per 400 altrimenti è bisestile se è divisibile per
#4 e non divisibile per 100. Non è bisestile negli altri casi.

anno = int(input("Inserisci un anno: "))


if anno <= 0 or anno >= 2100:
    print("Input non valido. L'anno deve essere compreso tra 1 e 2099.")
else:
    
    if anno % 400 == 0 or (anno % 4 == 0 and anno % 100 != 0):
        print(f"L'anno {anno} è bisestile.")
    else:
        print(f"L'anno {anno} non è bisestile.")