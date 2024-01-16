
def input_n() -> list[int]:
    n = int(input("Inserisci il numero di valori (n): "))
    valori = []
    for _ in range(n):
        valore = int(input("Inserisci un valore: "))
        valori.append(valore)
    return valori


def is_pari(num: int) -> bool:
    return num % 2 == 0


def somma_quadrati(lista_valori: list[int]) -> int:
    somma = 0
    for valore in lista_valori:
        if is_pari(valore):
            somma += valore ** 2
    return somma


valori_input = input_n()
print("Valori inseriti:", valori_input)

numero_test = 4
risultato_pari = is_pari(numero_test)
print(f"Il numero {numero_test} è pari? {risultato_pari}")

risultato_somma_quadrati = somma_quadrati(valori_input)
