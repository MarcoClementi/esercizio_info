import math

class VeicoloSpaziale:
    numero_veicoli = 0  

    def __init__(self, nome, velocita_massima, massa, posizione):
        self._nome = nome
        self._velocita_massima = velocita_massima
        self._massa = massa
        self._posizione = posizione
        VeicoloSpaziale.numero_veicoli += 1

    # Getter e Setter
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_velocita_massima(self):
        return self._velocita_massima

    def set_velocita_massima(self, velocita_massima):
        self._velocita_massima = velocita_massima

    def get_massa(self):
        return self._massa

    def set_massa(self, massa):
        self._massa = massa

    def get_posizione(self):
        return self._posizione

    def set_posizione(self, posizione):
        self._posizione = posizione

    def __str__(self):
        return f"{self._nome} - Velocità Massima: {self._velocita_massima} km/s - Massa: {self._massa} kg"

    def calcola_tempo_comunicazione(self, altro_veicolo):
        x1, y1, z1 = self._posizione
        x2, y2, z2 = altro_veicolo.get_posizione()
        distanza = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        tempo = distanza / 299792  
        return tempo

    @staticmethod
    def veicoli_totali():
        return VeicoloSpaziale.numero_veicoli

class Sonda(VeicoloSpaziale):
    def __init__(self, nome, velocita_massima, massa, posizione, tipo_missione, energia, consumo_energia):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._tipo_missione = tipo_missione
        self._energia = energia
        self._consumo_energia = consumo_energia

    # Getter e Setter
    def get_tipo_missione(self):
        return self._tipo_missione

    def set_tipo_missione(self, tipo_missione):
        self._tipo_missione = tipo_missione

    def get_energia(self):
        return self._energia

    def set_energia(self, energia):
        self._energia = energia

    def get_consumo_energia(self):
        return self._consumo_energia

    def set_consumo_energia(self, consumo_energia):
        self._consumo_energia = consumo_energia

    def __str__(self):
        return f"Sonda: {self._nome} - Velocità Massima: {self._velocita_massima} km/s - Massa: {self._massa} kg - Missione: {self._tipo_missione} - Energia: {self._energia} MJ"

    def simula_missione(self, durata):
        consumo = self._consumo_energia * durata
        if consumo <= self._energia:
            self._energia -= consumo
            return True
        return False

class Astronave(VeicoloSpaziale):
    def __init__(self, nome, velocita_massima, massa, posizione, numero_equipaggio, carburante, consumo_carburante):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._numero_equipaggio = numero_equipaggio
        self._carburante = carburante
        self._consumo_carburante = consumo_carburante

    # Getter e Setter
    def get_numero_equipaggio(self):
        return self._numero_equipaggio

    def set_numero_equipaggio(self, numero_equipaggio):
        self._numero_equipaggio = numero_equipaggio

    def get_carburante(self):
        return self._carburante

    def set_carburante(self, carburante):
        self._carburante = carburante

    def get_consumo_carburante(self):
        return self._consumo_carburante

    def set_consumo_carburante(self, consumo_carburante):
        self._consumo_carburante = consumo_carburante

    def __str__(self):
        return f"Astronave: {self._nome} - Velocità Massima: {self._velocita_massima} km/s - Massa: {self._massa} kg - Equipaggio: {self._numero_equipaggio} - Carburante: {self._carburante} t"

    def puo_raggiungere(self, distanza):
        carburante_necessario = distanza * self._consumo_carburante
        return carburante_necessario <= self._carburante

class StazioneOrbitante(VeicoloSpaziale):
    def __init__(self, nome, velocita_massima, massa, posizione, moduli, capacita_aggancio):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._moduli = moduli
        self._capacita_aggancio = capacita_aggancio
        self._veicoli_agganciati = []