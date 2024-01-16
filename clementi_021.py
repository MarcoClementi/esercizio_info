products = ["laptop", "mouse", "keyboard"]
prices = [1000, 50, 70]
quantities = [5, 10, 8]


print("Inventario attuale dei prodotti:")
for i in range(len(products)):
    print(f"Prodotto: {products[i]}, Prezzo: {prices[i]}, Quantità: {quantities[i]}")


prodotto = input("Inserisci il nome del prodotto da aggiungere/modificare: ")
prezzo = float(input("Inserisci il prezzo del prodotto: "))
quantità = int(input("Inserisci la quantità del prodotto: "))


if prodotto in products:

    index = products.index(prodotto)
    prices[index] = prezzo
    quantities[index] = quantità
else:
  
    products.append(prodotto)
    prices.append(prezzo)
    quantities.append(quantità)


prodotto_rimozione = input("Inserisci il nome del prodotto da rimuovere: ")
if prodotto_rimozione in products:

    index = products.index(prodotto_rimozione)
    del products[index]
    del prices[index]
    del quantities[index]
else:
    print("Il prodotto specificato non esiste nell'inventario.")


print("Inventario aggiornato dei prodotti:")
for i in range(len(products)):
    print(f"Prodotto: {products[i]}, Prezzo: {prices[i]}, Quantità: {quantities[i]}")


inventario_totale = sum(quantities)
print(f"Inventario totale: {inventario_totale}")


valore_totale = 0
for i in range(len(products)):
    valore_totale += prices[i] * quantities[i]
print(f"Valore totale delle azioni: {valore_totale}")
       

