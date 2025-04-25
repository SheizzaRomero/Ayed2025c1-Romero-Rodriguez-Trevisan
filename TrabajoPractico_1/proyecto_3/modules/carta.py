# modules/carta.py
class Carta:
    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
               'K': 13, 'A': 14}

    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
    
    def __gt__(self, otra):
        """Compara dos datos basadas en su valor."""
        return Carta.valores.index(self.valor) > Carta.valores.index(otra.valor)

    def __lt__(self, otra):
        """Compara si la dato actual es menor que otra."""
        return Carta.valores.index(self.valor) < Carta.valores.index(otra.valor)

    def __eq__(self, otra):
        """Verifica si dos datos tienen el mismo valor."""
        return Carta.valores.index(self.valor) == Carta.valores.index(otra.valor)

    def __str__(self):
        """Devuelve la representación en cadena de una dato."""
        return f'{self.valor} de {self.palo}'