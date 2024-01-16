IVA = 0.22

parco_auto = []

def aggiungi_auto(marca, modello, cilindrata, potenza_kw, anno_immatricolazione, costo_gestione, giorni_affitto, prezzo_giornaliero):
    auto = {
        "marca": marca,
        "modello": modello,
        "cilindrata": cilindrata,
        "potenza_kw": potenza_kw,
        "anno_immatricolazione": anno_immatricolazione,
        "costo_gestione": costo_gestione,
        "giorni_affitto": giorni_affitto,
        "prezzo_giornaliero": prezzo_giornaliero
    }
    parco_auto.append(auto)
    print(f"Auto {marca} {modello} aggiunta al parco auto.")

def rimuovi_auto(marca, modello):
    for auto in parco_auto:
        if auto["marca"] == marca and auto["modello"] == modello:
            parco_auto.remove(auto)
            print(f"Auto {marca} {modello} rimossa dal parco auto.")
            return
    print(f"Auto {marca} {modello} non trovata nel parco auto.")

def calcola_bollo(potenza_kw):
    if potenza_kw <= 100:
        bollo = 2.58 * potenza_kw
    elif potenza_kw <= 185:
        bollo = 2.58 * 100 + 3.87 * (potenza_kw - 100)
    else:
        bollo = 2.58 * 100 + 3.87 * 85 + 20 * (potenza_kw - 185)
    return bollo

def calcola_profitto_auto(auto):
    bollo = calcola_bollo(auto["potenza_kw"])
    profitto = auto["giorni_affitto"] * (auto["prezzo_giornaliero"] - IVA) - auto["costo_gestione"] - bollo
    return profitto

def calcola_profitto_totale():
    profitto_totale = 0
    for auto in parco_auto:
        profitto_totale += calcola_profitto_auto(auto)
    return profitto_totale

# Esempio di utilizzo:
aggiungi_auto("Toyota", "Corolla", 1600, 80, 2020, 500, 7, 50)
aggiungi_auto("BMW", "X5", 3000, 200, 2022, 800, 5, 120)

rimuovi_auto("Toyota", "Corolla")

profitto_totale = calcola_profitto_totale()
print(f"Profitto totale del parco auto (prima delle tasse): {profitto_totale} euro")
