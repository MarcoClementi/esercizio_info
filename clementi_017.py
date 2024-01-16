n = int(input("Inserisci il numero di valori da inserire nella lista: "))
lista = []
for i in range(n):
    valore = input("Inserisci un valore: ")
    lista.append(valore)

valore_cercato = input("Inserisci il valore da cercare: ")
if valore_cercato in lista:
    print("Valore presente")
else:
    print("Valore non presente")