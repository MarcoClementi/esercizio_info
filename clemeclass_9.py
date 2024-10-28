class Libro:
    def __init__(self, titolo, autore, pagine):
        self._titolo = None
        self._autore = None
        self._pagine = None
        
        self.titolo = titolo  
        self.autore = autore  
        self.pagine = pagine   

    @property
    def titolo(self):
        return self._titolo

    @titolo.setter
    def titolo(self, valore):
        if not valore:
            raise ValueError("Il titolo non può essere una stringa vuota.")
        self._titolo = valore

    @property
    def autore(self):
        return self._autore

    @autore.setter
    def autore(self, valore):
        if not valore:
            raise ValueError("L'autore non può essere una stringa vuota.")
        self._autore = valore

    @property
    def pagine(self):
        return self._pagine

    @pagine.setter
    def pagine(self, valore):
        if valore <= 0:
            raise ValueError("Il numero di pagine deve essere un numero positivo.")
        self._pagine = valore

try:
    libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
    print(libro.titolo) 
    libro.titolo = "Lo Hobbit"  
    print(libro.titolo)
    
    
    libro.titolo = ""  
except ValueError as e:
    print(e)
