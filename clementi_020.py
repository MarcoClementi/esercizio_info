#Scrivere un programma che permetta la gestione di una lista della spesa. Esso deve prevedere un men così formato:

"""
Scegliere l'opzione desiderata:
1) Visualizza lista
2) Aggiungi item e quantità
3) Modifica quantità di un item
4) Rimuovi item
5) Esci
Scelta:_

"""


lista_spesa = []
quantita_spesa = []

while True:
  
    print("""
Scegliere l'opzione desiderata:
1) Visualizza lista
2) Aggiungi item e quantità
3) Modifica quantità di un item
4) Rimuovi item
5) Esci
    """)

    scelta = input("Scelta: ")

    if scelta == "1":
        
        print("Lista della spesa:")
        for i in range(len(lista_spesa)):
            print(f"{lista_spesa[i]} - {quantita_spesa[i]}")

    elif scelta == "2":
        
        item = input("Inserisci l'item: ")
        quantita = input("Inserisci la quantità: ")
        lista_spesa.append(item)
        quantita_spesa.append(quantita)
        print("Item aggiunto alla lista della spesa.")

    elif scelta == "3":
        
        index = int(input("Inserisci l'indice dell'item da modificare: "))
        if index < len(lista_spesa):
            nuova_quantita = input("Inserisci la nuova quantità: ")
            quantita_spesa[index] = nuova_quantita
            print("Quantità modificata.")
        else:
            print("Indice non valido.")

    elif scelta == "4":
        
        index = int(input("Inserisci l'indice dell'item da rimuovere: "))
        if index < len(lista_spesa):
            del lista_spesa[index]
            del quantita_spesa[index]
            print("Item rimosso dalla lista della spesa.")
        else:
            print("Indice non valido.")

    elif scelta == "5":
       
        break

    else:
        print("Scelta non valida. Riprovare.")