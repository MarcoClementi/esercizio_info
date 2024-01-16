numero = int(input("Quanti valori vuoi inserire? "))

lista = []
for i in range(numero):
    valore = int(input("Inserisci il valore: "))
    lista.append(valore)

somma = 0
massimo = float('-inf')
minimo = float('inf')

for valore in lista:
    somma += valore
    if valore > massimo:
        massimo = valore
    if valore < minimo:
        minimo = valore

media = somma / numero

print("Valore medio:", media)
print("Massimo:", massimo)
print("Minimo:", minimo)