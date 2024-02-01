#Sulla base di quanto visto a lezione sul modulo random realizzare un programma che implementi il gioco della tombola o del bingo. 
#Al fine di far ciò, lo studente implementi le seguenti funzioni:
#1) def genera_cartella(id: int<str>)->dict:
#La funzione genera una cartella della tombola/bingo e la restituisce come dizionario. Dare un id alla cartella.
#N.B.
#La cartella ha le seguenti caratteristiche:
#1) 3 righe e 9 colonne
#2) 15 numeri in totale (5 per riga)
#3) ogni colonna ha solo i numeri della decina di riferimento: la prima dall'1 al 10, la seconda dal 11 al 20....l'ultima dall'81 al 90
#2) def estrai_numero(numeri_estratti: list[])->int:
#La funzione estrae un nuovo numero, lo inserisce nella lista passata come parametro, controllando che non sia duplicato, e restituisce tale numero come intero.
#3) def controlla_cartella(cartella: dict, numeri_estratti[])->list[bool]:
#Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella. Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, l'1 al terno fino ad arrivare al 4 che si riferisce alla tombola/bingo.
#es.
#[True, True, False, False, False] per una cartella che ha fatto terno(naturalmente per fare terno bisogna aver fatto anche ambo....)
#Realizzare un programma che implementi la logica di funzionamento:
#a) Utilizzando le opportune variabili di stato (es. una lista di cartelle, la lista dei numeri estratti, lo stato del gioco(ambo, terno,....))
#b) Utilizzando le funzioni precedentemente definite al fine di gestire le varie fasi del gioco.

import random

def genera_cartella(id):
    cartella = {}
    numeri_generati = set()
    for i in range(3):
        riga = []
        while len(riga) < 5:
            num = random.randint(i*10+1, i*10+10)
            if num not in numeri_generati:
                riga.append(num)
                numeri_generati.add(num)
        riga.sort()
        cartella[i] = riga
    return {id: cartella}

def estrai_numero(numeri_estratti):
    num = random.randint(1, 90)
    while num in numeri_estratti:
        num = random.randint(1, 90)
    numeri_estratti.append(num)
    return num

def controlla_cartella(cartella, numeri_estratti):
    stato = [False] * 4
    for riga in cartella.values():
        if set(riga).issubset(set(numeri_estratti)):
            if stato[0] == False: stato[0] = True
            elif stato[1] == False: stato[1] = True
            elif stato[2] == False: stato[2] = True
            else: stato[3] = True
    return stato


numeri_estratti = []
cartelle = []

for i in range(5):
    cartelle.append(genera_cartella(str(i+1)))

while True:
    num = estrai_numero(numeri_estratti)
    print("Numero estratto:", num)
    for i, cartella in enumerate(cartelle):
        stato = controlla_cartella(cartella[str(i+1)], numeri_estratti)
        if stato != [False] * 4:
            print("Cartella", i+1, ":", stato)
    
    if [True] * 4 in [controlla_cartella(cartella[str(i+1)], numeri_estratti) for i, cartella in enumerate(cartelle)]:
        print("BINGO!")
        break






   

