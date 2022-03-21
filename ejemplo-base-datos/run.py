from bd import *
import codecs
import random


class Ejecutor:

    def ver_data(self):
        base = BDdatos()
        print(base.obtener_datos_dos("apps_countries"))

    def agregar_valores(self):
        base = BDdatos()
        base.agregar_datos(["RE", "Demo País"], "apps_countries")


    def agregar_valores_dos(self):
        base = BDdatos()
        base.agregar_datos_dos(["usuario002", 200.2], "estudiantes")

if __name__ == '__main__':
    """
    """
    #
    objeto = Ejecutor()
    # objeto.ver_data()
    objeto.agregar_valores_dos()
