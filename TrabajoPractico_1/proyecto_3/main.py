# main.py
from modules.juegoGuerra import JuegoGuerra

if __name__ == "__main__":
    juego = JuegoGuerra(random_seed=314)
    juego.iniciar_juego(ver_partida=False)
    print(f"Turnos jugados: {juego.turnos_jugados}")
    print(f"Ganador: {juego.ganador}")
    print(f"Empate: {juego.empate}")
