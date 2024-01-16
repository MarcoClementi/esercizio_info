#In una copisteria, il costo unitario delle fotocopie varia a seconda del numero da effettuare secondo la seguente tabella:
numero_fotocopie = int(input("Inserisci il numero di fotocopie da effettuare: "))
nome_cliente = input("Inserisci il nome del cliente: ")
rilegatura = input("Il plico è da rilegare? (s/n) ")

# Calcolo del costo totale
if numero_fotocopie >= 1 and numero_fotocopie <= 19:
    costo_unitario = 0.10
elif numero_fotocopie >= 20 and numero_fotocopie <= 100:
    costo_unitario = 0.08
else:
    costo_unitario = 0.05

costo_totale = numero_fotocopie * costo_unitario

if rilegatura == "s":
    costo_totale += 1.80

# Stampa del prospetto
print("Gentile Sig. " + nome_cliente + ", il suo preventivo è di " + str(costo_totale) + " euro", end="")
if rilegatura == "s":
    print(" compresa la rilegatura.")
else:
    print(".")