#Dato in input un numero scritto con sistema di numerazione decimale (intero), calcolare la sua conversione in binario. 
# Dato che la stampa a video del numero deve avvenire in ordine inverso da quello del calcolo,
# usare una lista per stampare il valore corretto
numero_decimale = int(input("Inserisci un numero decimale: "))  

numero_binario = []  

while numero_decimale > 0:  
    bit = numero_decimale % 2  
    numero_binario.append(bit)  
    numero_decimale = numero_decimale // 2  

for bit in reversed(numero_binario):
    print(bit, end="")

print()  