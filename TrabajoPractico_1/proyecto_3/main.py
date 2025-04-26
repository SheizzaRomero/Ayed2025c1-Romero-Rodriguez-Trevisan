from modules.moduloguerra import JuegoGuerra

if __name__ == "__main__":
    juego = JuegoGuerra(random_seed=42)
    juego.iniciar_juego(ver_partida=True)

# Mostrar resultados
    print(f"Turnos jugados: {juego.turnos_jugados}")
    if juego.empate:
        print("El juego terminó en empate.")
    else:
        print(f"El ganador es: {juego.ganador}")