from modules.AVL import NodoArbol, ArbolBinarioBusqueda_AVL
from datetime import date
from modules.Temperaturas_DB import Temperaturas_DB

def main():
    db = Temperaturas_DB()

    db.guardar_temperatura(30.1, date (2023,5,1))
    db.guardar_temperatura(25.4, date (2023,6,1))
    db.guardar_temperatura(28.7, date (2023,7,1))
    db.guardar_temperatura(22.5, date (2023,8,1))
    db.guardar_temperatura(18.3, date (2023,9,1))
    db.guardar_temperatura(19.2, date (2023,10,1))

    print("Temperaturas guardadas:")
    print ("Maximo del rango" , db.max_temp_rango(date (2023,7,1), date (2023,9,1) ))
    

if __name__ == "__main__":
   main ()

