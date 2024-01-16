dipendenti = [
    {"nome": "Marco Clementi", "ruolo": "Programmatore", "stipendio": 2000},
    {"nome": "Aron Bologna", "ruolo": "Designer", "stipendio": 1800},
    {"nome": "Fabio Bilancioni", "ruolo": "Project Manager", "stipendio": 2500}
]    

print("Lista dei dipendenti")
for dipendente in dipendenti:
      print(dipendente["nome"], "-", dipendente["ruolo"])
      
progetto = {"budget": 10000, "costo_orario": 50, "ore_lavorate": 0}
azienda = {"dipendenti": dipendenti, "progetto": progetto}

for dipendente in azienda["dipendenti"]:
    ore_lavorate = int(input(f"Inserisci le ore lavorate da {dipendente['nome']} sul nuovo progetto: "))
    costo_dipendente = ore_lavorate * azienda["progetto"]["costo_orario"]
    dipendente["stipendio"] += costo_dipendente
    azienda["progetto"]["budget"] -= costo_dipendente
    dipendente["ore_lavorate"] = ore_lavorate
    
    print("\nLista dei dipendenti con stipendi totali e ore lavorate:")
for dipendente in azienda["dipendenti"]:
    print(dipendente["nome"], "-", dipendente["stipendio"], "euro -", dipendente["ore_lavorate"], "ore")
    
    print("\nStatistiche del progetto:")
ore_totali = sum(dipendente["ore_lavorate"] for dipendente in azienda["dipendenti"])
budget_restante = azienda["progetto"]["budget"]
print("Ore totali lavorate:", ore_totali)
print("Budget rimanente:", budget_restante)

