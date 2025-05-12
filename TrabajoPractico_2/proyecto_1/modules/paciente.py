from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self, orden):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__orden_de_llegada = orden

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
        cad += str(self.__riesgo) + ' - ' + self.__descripcion
        return cad

    def __repr__(self):
        return f"{self.__nombre} {self.__apellido} - riesgo({self.__riesgo})"