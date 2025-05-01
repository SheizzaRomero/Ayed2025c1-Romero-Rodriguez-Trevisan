# carta.py

class Carta:
    
    def __init__(self, valor='', palo=''):
        self.valor = valor
        self.palo = palo
        self.visible: bool = False

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        self._visible = visible

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, palo):
        self._palo = palo

    def _valor_numerico(self):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return valores.index(self.valor)

    def __gt__(self, otra):
        """Comparación por valor numérico"""
        return self._valor_numerico() > otra._valor_numerico()

    def __str__(self):
        return self.valor + self.palo if self.visible else "-X"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    carta = Carta("3", "♣")
    print(carta)
    carta.visible = True
    print(carta)
