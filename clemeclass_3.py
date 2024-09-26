class Veicolo:
    numero_veicoli = 0  

    def __init__(self, tipo, marca):
        Veicolo.numero_veicoli += 1  
        self.tipo = tipo
        self.marca = marca

    @classmethod
    def get_numero_veicoli(cls):
        return cls.numero_veicoli

print(Veicolo.get_numero_veicoli())  
auto1 = Veicolo("Auto", "Toyota")
auto2 = Veicolo("Moto", "Honda")
print(Veicolo.get_numero_veicoli())  