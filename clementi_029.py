def calcola_importo(fatture: list[dict]) -> list[float] | None:
    if not fatture:
        return None

    totale_importi = 0
    totale_importi_scontati = 0

    for fattura in fatture:
        importo = fattura["importo"]
        sconto_percentuale = fattura["sconto_fattura"]
        importo_scontato = importo * (1 - sconto_percentuale / 100)

        fattura["importo_scontato"] = importo_scontato

        totale_importi += importo
        totale_importi_scontati += importo_scontato

    return [totale_importi, totale_importi_scontati]



fatture = [
    {"id": "Monticelli", "importo": 245.78, "sconto_fattura": 10},
    {"id": "Kola", "importo": 325.71, "sconto_fattura": 12},
    {"id": "Romagna", "importo": 245.78, "sconto_fattura": 8},
    {"id": "Bilancioni", "importo": 245.78, "sconto_fattura": 15},
    {"id": "Sanchi", "importo": 245.78, "sconto_fattura": 5},
    {"id": "Pontellini", "importo": 245.78, "sconto_fattura": 18},
    {"id": "Clementi", "importo": 245.78, "sconto_fattura": 20},
    {"id": "Arlotti", "importo": 245.78, "sconto_fattura": 19},
    {"id": "Nedria", "importo": 245.78, "sconto_fattura": 7},
    {"id": "Santini", "importo": 245.78, "sconto_fattura": 22},
]


risultato = calcola_importo(fatture)

if risultato is not None:
    print("Totale Importi:", risultato[0])
    print("Totale Importi Scontati:", risultato[1])
else:
    print("La lista delle fatture è vuota.")
