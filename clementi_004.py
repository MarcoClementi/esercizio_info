numero_persone = int(input("Inserire il numero di persone nel gruppo: "))

spesa_adulti = 10 * numero_persone
spesa_minorenni = 6 * numero_persone

spesa_complessiva = spesa_adulti + spesa_minorenni

print("La spesa complessiva per il gruppo di", numero_persone, "persone è di", spesa_complessiva, "euro.")