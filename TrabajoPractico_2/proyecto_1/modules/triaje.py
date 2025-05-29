# archivo: triaje.py

import msvcrt
import monticulo, paciente as pac

class SalaEmergencia:
    """SalaEmergencia: administra una cola de acuerdo a la prioridad y el orden de llegada"""
    def __init__(self):
        self.__cola = monticulo.MonticuloBinario()

    def ingresarPaciente(self, p_paciente:pac.Paciente=None):
        """ingresarPaciente: ingresa un nuevo paciente a la sala"""
        if p_paciente is None:
            p_paciente = pac.Paciente()
        self.__cola.insertar(p_paciente)

    def atenderPaciente(self) -> pac.Paciente:
        """atenderPaciente: un paciente es atendido; se lo quita de la cola"""
        return self.__cola.eliminarMinimo()

    @property
    def pacientesEsperando(self) -> int:
        return len(self.__cola)

if __name__ == '__main__':
    print('* PRUEBA: inicio')

    print ('instrucciones:')
    print('- I : ingresa un paciente')
    print('- A : se atiende un paciente')
    print('- cualquier otra tecla sale de la prueba')
    print('---')

    salita = SalaEmergencia()
    continuar = True
    while continuar:
        tecla = msvcrt.getch()
        if tecla == b'I' or tecla == b'i':   # ingresa un paciente
            p = pac.Paciente()
            print('ingresa paciente:', str(p))
            salita.ingresarPaciente(p)
        elif tecla == b'A' or tecla == b'a':   # se atiende un paciente
            print('paciente atendido:', str(salita.atenderPaciente()))
        else:
            continuar = False
        print('pacientes esperando:', salita.pacientesEsperando)
        print('---')

    print('* PRUEBA: fin')