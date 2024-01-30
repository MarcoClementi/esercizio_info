import random

def lancio_moneta():
    
    risultato = random.randint(0, 1)


    if risultato == 0:
        return "Testa"
    else:
        return "Croce"

risultato_lancio = lancio_moneta()
print(f"Il risultato del lancio è: {risultato_lancio}")
