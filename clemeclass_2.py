class ContoBancario:
    def __init__(self, numero_conto, intestatario, saldo):
        self.numero_conto = numero_conto
        self.intestatario = intestatario
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def deposita(self, importo):
        self._saldo += importo

    def preleva(self, importo):
        if self._saldo - importo < 0:
            print("Errore: saldo insufficiente")
        else:
            self._saldo -= importo

# Esempio di utilizzo
conto = ContoBancario("123456789", "Mario Rossi", 1000.0)
print(conto.get_saldo())  # Output: 1000.0
conto.deposita(500.0)
print(conto.get_saldo())  # Output: 1500.0
conto.preleva(200.0)
print(conto.get_saldo())  # Output: 1300.0