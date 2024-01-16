import os
lista_item = []
lista_quant = []
menu = 0
while menu != 5:
    os.system('cls'if os.name == 'nt' else 'clear')
   
    print("Scegliere l'opzione desiderata:")
    print("1) Visualizza lista")
    print("2) Aggiungi item e quantità")
    print("3) Modifica quantità di un item")
    print("4) Rimuovi item")
    print("5) Esci")

    len_item = len(lista_item)
    len_quant = len(lista_quant)
    menu = int(input("Scelta: "))
    if menu == 1:
        x = zip(lista_quant, lista_item)
        print("Questa è la tua lista.\n",tuple (x))
    elif menu == 2:
        item = str(input("Scegliere un prodotto: "))
        quant = int(input("Inserisci la quantità del prodotto: "))
        lista_quant.append(quant)
        lista_item.append(item)
        print("Prodotto aggiunto")
    elif menu == 3:
        index = int(input("Selezionare l'indice del prodotto da modificare: "))
        index -= 1
        if index <= len(lista_item):
            mod_quant = int(input("Inserisci la quantità del prodotto:  "))
            lista_quant[index] = mod_quant
            print(f"Quantità modificata.")
        else:
            print("Prodotto non trovato.")
    elif menu == 4:
        elim = int(input("Selezione l'indice del prodotto da eliminare: "))
        elim -= 1
        if elim <= len(lista_item):
            del lista_item[elim]
            del lista_quant[elim]
            print(f"Prodotto eliminato")
        else:
            print("Prodotto non trovato.")
    elif menu == 5:
        break
    else:
        print("Istruzione non valida, riprova.")
    input("Premere INVIO per continuare...")
print("Grazie per aver usato LISTA_PYTHON.")