class Frazione:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, altro):
        return Frazione(self.x * altro.y + altro.x * self.y, self.y * altro.y)

    def __sub__(self, altro):
        return Frazione(self.x * altro.y - altro.x * self.y, self.y * altro.y)

    def __mul__(self, altro):
        return Frazione(self.x * altro.x, self.y * altro.y)

    def __str__(self):
        return f"Frazione({self.x}, {self.y})"

# Esempio di utilizzo
f1 = Frazione(3, 4)
f2 = Frazione(2, 4)

# Addizione
f3 = f1 + f2
print(f3)  # Output: Frazione(20, 16)

# Sottrazione
f4 = f1 - f2
print(f4)  # Output: Frazione(4, 16)

# Moltiplicazione
f5 = f1 * f2
print(f5)  # Output: Frazione(6, 16)

# Rappresentazione
print(f1)  # Output: Frazione(3, 4)