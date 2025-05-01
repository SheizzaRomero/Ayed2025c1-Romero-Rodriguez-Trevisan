# main.py

from juego_guerra import JuegoGuerra
import random

def main():
    print("===== JUEGO DE GUERRA =====")
    print("Iniciando partida...\n")

    # Semilla aleatoria para reproducibilidad
    semilla = random.randint(0, 1000)
    print(f"Semilla utilizada: {semilla}\n")

    juego = JuegoGuerra(random_seed=semilla)
    juego.iniciar_juego(ver_partida=True)

    print("\n===== RESULTADO FINAL =====")
    print(f"Turnos jugados: {juego.turnos_jugados}")
    if juego.empate:
        print("Resultado: Empate")
    else:
        print(f"Ganador: {juego.ganador}")

if __name__ == "__main__":
    main()
