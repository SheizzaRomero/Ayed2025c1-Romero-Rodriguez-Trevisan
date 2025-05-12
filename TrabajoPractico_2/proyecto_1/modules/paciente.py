from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antony', 'Estela', 'Jorge', 'Augusta']
apellidos = ['Perez', 'Colman', 'Rodrin', 'Juarez', 'García', 'Velgro', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    """Paciente: la clase lleva el control del orden de llegada"""
    __orden = 0
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        Paciente.__orden += 1
        self.__orden_de_llegada = Paciente.__orden

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_riesgo(self):
        return self.__riesgo

    def get_descripcion_riesgo(self):
        return self.__descripcion

    def __lt__(self, otro):
        salida = False
        if self.__riesgo == otro.__riesgo:
            if self.__orden_de_llegada < otro.__orden_de_llegada:
                salida = True
        elif self.__riesgo < otro.__riesgo:
            salida = True
        return salida

    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> ord. ' + str(self.__orden_de_llegada)
        cad += ' - ' + self.__descripcion
        return cad

    def __repr__(self):
        return f"{self.__nombre} {self.__apellido} - riesgo({self.__riesgo})"