class Pagamento: 
    def processo_pagamento(self, valore_da_pagare: float):
        raise NotImplementedError("Questo metodo deve essere sovrascritto")

class CartaDiCredito(Pagamento):
    def __init__(self, nome, numero, data, cvv):
        self.nome = nome
        self.numero = numero
        self.data = data
        self.cvv = cvv

    def processo_pagamento(self, valore_da_pagare: float):
        print(f"Elaborazione Carta di Credito per {self.nome}")

class PayPal(Pagamento):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def processo_pagamento(self, valore_da_pagare: float):
        print(f"Elaborazione PayPal per {self.email}")
# Esempio di utilizzo
def effettua_pagamento(metodo_di_pagamento: Pagamento):
    metodo_di_pagamento.processo_pagamento( 100.0 )

pagamento_carta = CartaDiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

effettua_pagamento(pagamento_carta)  # Output: Elaborazione pagamento con Carta di Credito per Mario Rossi
effettua_pagamento(pagamento_paypal)  # Output: Elaborazione pagamento con PayPal per mario.rossi@example.com