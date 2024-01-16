numero = int(input("Inserisci il valore:"))
lista = []


for i in range(numero):
    valore = input("Inserisci un valore:")
    lista.append(valore)
    
print("La lista è:")
for elemento in lista:
    print(elemento)