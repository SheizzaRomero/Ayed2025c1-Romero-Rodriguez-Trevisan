# archivo: triaje.py

import monticulo, paciente as pac

class SalaEmergencia:
    """SalaEmergencia: administra una cola de acuerdo a prioridad y orden de llegada"""
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

    salita = SalaEmergencia()

    print('\n...ingresan cinco pacientes')
    for _ in range(5):
        p = pac.Paciente()
        print(str(p))
        salita.ingresarPaciente(p)

    print('\n...se atiende un paciente')
    print(str(salita.atenderPaciente()))

    print('\n...se atiende otro paciente')
    print(str(salita.atenderPaciente()))

    print('\n...ingresa un paciente')
    p = pac.Paciente()
    print(str(p))
    salita.ingresarPaciente(p)

    print('\n...se atiende un tercer paciente')
    print(str(salita.atenderPaciente()))

    print('\n...cantidad de pacientes esperando:', salita.pacientesEsperando)

    print('* PRUEBA: fin')