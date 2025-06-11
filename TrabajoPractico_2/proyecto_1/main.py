# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time, datetime, random
from modules import paciente as pac
from modules.triaje import SalaEmergencia

n = 20  # cantidad de ciclos de simulación

sala = SalaEmergencia()

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()
    print ('Se crea un paciente:', paciente)
    sala.ingresarPaciente(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5 and sala.pacientesEsperando > 0:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = sala.atenderPaciente()
        print('*' * 40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*' * 40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass

    print()

    # Se muestran los pacientes restantes en la cola de espera
    print()
    print('Pacientes que faltan atenderse:', sala.pacientesEsperando) 

    print()
    print('-*-'*15)

    time.sleep(1)