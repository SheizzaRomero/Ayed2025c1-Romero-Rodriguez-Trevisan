# modules/juegoGuerra.py
import random
from modules.mazo import Mazo
from modules.carta import Carta

class JuegoGuerra:
    def __init__(self, random_seed=None):
        self.mazo_completo = Mazo()
        self.jugador1 = Mazo()
        self.jugador2 = Mazo()
        self.turnos_jugados = 0
        self.ganador = None
        self.empate = False
        self.random_seed = random_seed
        if random_seed is not None:
            random.seed(random_seed)
        self.repartir_cartas()

    def repartir_cartas(self):
        """Reparte las cartas del mazo entre los dos jugadores."""
        while len(self.mazo_completo) > 0:
            self.jugador1.append(self.mazo_completo.sacar_carta_arriba())
            if len(self.mazo_completo) > 0:
                self.jugador2.append(self.mazo_completo.sacar_carta_arriba())

    def iniciar_juego(self, ver_partida=False, velocidad=0.1):
        """Inicia la partida simulando turnos hasta que un jugador gane o haya empate.
        - ver_partida: Si es True, muestra cada turno en detalle.
        - velocidad: Tiempo de espera entre cada ronda en segundos (solo si ver_partida=True)."""
        import time

        while len(self.jugador1) > 0 and len(self.jugador2) > 0:
            self.turnos_jugados += 1

            if ver_partida:
                print(f"\nTurno {self.turnos_jugados}")
                print(f"Jugador 1 tiene {len(self.jugador1)} cartas.")
                print(f"Jugador 2 tiene {len(self.jugador2)} cartas.")

            carta_jugador1 = self.jugador1.pop(0)
            carta_jugador2 = self.jugador2.pop(0)

            if ver_partida:
                print(f"Jugador 1 juega: {carta_jugador1}")
                print(f"Jugador 2 juega: {carta_jugador2}")

            if carta_jugador1 > carta_jugador2:
                self.jugador1.extend([carta_jugador1, carta_jugador2])  # Gana jugador 1
                if ver_partida:
                    print("Jugador 1 gana esta ronda.")
            elif carta_jugador2 > carta_jugador1:
                self.jugador2.extend([carta_jugador1, carta_jugador2])  # Gana jugador 2
                if ver_partida:
                    print("Jugador 2 gana esta ronda.")
            else:
                if ver_partida:
                    print("Empate en esta ronda, las cartas se descartan.")

            if ver_partida:
                print(f"Jugador 1 tiene {len(self.jugador1)} cartas restantes.")
                print(f"Jugador 2 tiene {len(self.jugador2)} cartas restantes.")
                print("-" * 30)
                time.sleep(velocidad)  # Pausa entre rondas para visualizar mejor el proceso

        # Determinar el resultado final
        if len(self.jugador1) > len(self.jugador2):
            self.ganador = 'jugador 1'
            print("\n¡Jugador 1 gana el juego!")
        elif len(self.jugador2) > len(self.jugador1):
            self.ganador = 'jugador 2'
            print("\n¡Jugador 2 gana el juego!")
        else:
            self.empate = True
            print("\nEl juego ha terminado en empate.")
