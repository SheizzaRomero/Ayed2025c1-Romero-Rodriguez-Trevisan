from modules.AVL import NodoArbol, ArbolBinarioBusqueda_AVL
from datetime import date
from modules.Temperaturas_DB import Temperaturas_DB

db = Temperaturas_DB()

db.guardar_temperatura(30.1, date (2023,5,1))
db.guardar_temperatura(25.4, date (2023,6,1))
db.guardar_temperatura(28.7, date (2023,7,1))
db.guardar_temperatura(22.5, date (2023,8,1))
db.guardar_temperatura(18.3, date (2023,9,1))
db.guardar_temperatura(19.2, date (2023,10,1))
print("Temperaturas guardadas:")

print("Devolver temperatura del 1/6/2023")
print(db.devolver_temperatura(date(2023,6,1)))

print ("Maximo del rango" , db.max_temp_rango(date (2023,7,1), date (2023,9,1) ))

print ("Mínimo del rango" , db.min_temp_rango(date (2023,7,1), date (2023,9,1) ))

print ("Temperaturas extremas del rango" , db.temp_extremos_rango(date (2023,6,1), date (2023,9,1) ))
    
print("Listado de temperaturas:")
for linea in db.devolver_temperaturas(date(2023,6,1), date(2023,9,1)):
    print(linea)

print("Borrar la temperatura del 1/7/2023")
del(db[date(2023,7,1)])

print("Listado de temperaturas:")
for linea in db.devolver_temperaturas(date(2023,6,1), date(2023,9,1)):
    print(linea)

print("Cantidad de muestras:", db.cantidad_muestras())
