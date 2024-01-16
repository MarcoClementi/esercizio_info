#Scrivere un programma che passati in input un numero non definito a priori di voti, ne calcoli la media.
# Il programma terminerà con l'iterazione degli input quando inseriamo un valore <=0.
# Non si  considerino ai fini della media, i voti >10.

numero_voti = 0
somma_voti = 0
voto = float(input("inserire voto: "))
while voto > 0:
    if (voto <= 10):
        numero_voti += 1
        somma_voti += voto
    voto = float(input("inserire voto: "))      
media = somma_voti / numero_voti
print(f"la tua media è di {media}")

