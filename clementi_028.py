def calcola_superbollo (kW:int, immatricolazione: int) ->float:

 anno_corrente = 2023
 anni_passati = anno_corrente - immatricolazione

 if anni_passati < 0:
  return None
 
 if anni_passati < 5:
   costo_kw = 20

 if anni_passati < 10:
  costo_kw = 12

 if anni_passati < 15:
  costo_kw = 6  

 if anni_passati <= 15:
  
  return 0
    
 else:
  
  return None
  
  return (kw - 185) * costo_per_kw
 
 def calcola_bollo (classe_ambientale:int, kW:int, immatricolazione:int) ->list[float] | None:
  
  if classe_ambientale not in range(0,7):
   return None
  
  base_kw = {
   
   0:3,
   1:2.9,
   2:2.8,
   3:2.7,
   4:2.58,
   5:2.58,
   6:2.58

  }

  aggiuntivo_kw = {
   
   0:4.5,
   1:4.35,
   2:4.2,
   3:4.05,
   4:3.87,
   5:3.87,
   6:3.87,
  
    }

  kw_sotto_i_100 = kW if kW < 100 else 100  
 
  kw_oltre_i_100 = kW - kw_sotto_i_cento
    
  costo_bollo = (costo_base_per_kw[classe_ambientale] + (costo_aggiuntivo_per_kw[classe_ambientale] if kw_oltre_i_100 > 0 else 0)) * kw_sotto_i_100
  costo_superbollo = calcola_superbollo(kw, immatricolazione)

  return [costo_bollo, costo_superbollo] if costo_superbollo is not None else None



 bollo, superbollo = calcola_bollo(classe_ambientale=0, kw=120, immatricolazione=2018)
 if bollo is not None and superbollo is not None:
    print(f'Bollo: {bollo}, Superbollo: {superbollo}')
 else:
    print('Dati non validi oppure non è previsto il superbollo')