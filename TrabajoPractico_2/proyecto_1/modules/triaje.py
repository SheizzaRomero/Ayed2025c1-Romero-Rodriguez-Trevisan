# archivo: triaje.py

import monticulo, paciente as pac

class SalaEmergencia:
    """SalaEmergencia: administra una cola de acuerdo a prioridad y orden de llegada"""
    def __init__(self):
        self.__cola = monticulo.MonticuloBinario()

    def aceptarPaciente(self, p_paciente:pac.Paciente=None):
        """aceptarPaciente: ingresa un nuevo paciente a la sala"""
        if p_paciente is None:
            p_paciente = pac.Paciente()
        self.__cola.insertar(p_paciente)

    def atenderPaciente(self) -> pac.Paciente:
        """aceptarPaciente: un paciente es atendido; se lo quita de la cola"""
        return self.__cola.eliminarMinimo()

    @property
    def cola(self) -> str:
        return str(self.__cola)

if __name__ == '__main__':
    print('* PRUEBA: inicio')

    salita = SalaEmergencia()
    for _ in range(3):
        p = pac.Paciente()
        print(str(p))
        salita.aceptarPaciente(p)
    print(salita.cola)

    print('* PRUEBA: fin')