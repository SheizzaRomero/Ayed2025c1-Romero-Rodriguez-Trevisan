from modules.AVL import NodoArbol, ArbolBinarioBusqueda_AVL
from modules.Temperaturas_DB import Temperaturas_DB

def main():
    db = Temperaturas_DB()

    db.guardar_temperatura(30.1, "05/01/2023")
    db.guardar_temperatura(25.4, "06/01/2023")
    db.guardar_temperatura(28.7, "07/01/2023")

    print("Temperaturas guardadas:")
    for fecha in ["05/01/2023", "06/01/2023", "07/01/2023"]:
        print(f"{fecha}: {db.obtener_temperatura(fecha)} °C")

if __name__ == "__main__":
    main()

