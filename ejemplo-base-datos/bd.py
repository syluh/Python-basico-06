# -*- coding: utf-8 -*-
import codecs
from config import *
import mysql.connector as database


class BDdatos():
    """
        Clase para la Base de Datos
    """
    def conectar(self):
        """
           conectarme a la bd
        """
        db = None
        try:
            # obtener datos de autentificacion de la base de datos
            host = HOST
            user = USER
            clave = PASS
            base_datos = BD
            db = database.connect(database=base_datos, user=user, host=host, \
            password=clave)
        except Exception(e):
            print("error de coneccion", e)
        return db

    def obtener_datos(self, tabla):
        """
            conectarme a la bd, para sacar los datos necesarios
        """
        db = self.conectar()
        cursor = db.cursor()
        sql = "select * from %s;" % tabla
        cursor.execute(sql)
        datos = cursor.fetchall()
        db.close()
        return datos


    def obtener_datos_dos(self, tabla):
        """
            conectarme a la bd, para sacar los datos necesarios
        """
        db = self.conectar()
        cursor = db.cursor(dictionary=True)
        sql = "select * from %s;" % tabla
        cursor.execute(sql)
        datos = cursor.fetchall()
        db.close()
        return datos


    def agregar_datos(self, datos, tabla):
        """
        """
        db = self.conectar()
        cursor = db.cursor()
        sql = """INSERT INTO %s (country_code, country_name)
                VALUES ('%s', '%s');""" % (tabla, datos[0], datos[1])
        m = cursor.execute(sql)
        # print(m)
        db.commit()
        db.close()


    def agregar_datos_dos(self, datos, tabla):
        """
        """
        db = self.conectar()
        cursor = db.cursor()
        sql = """INSERT INTO %s (usuario, sueldo)
                VALUES ('%s', %.2f);""" % (tabla, datos[0], datos[1])
        m = cursor.execute(sql)
        # print(m)
        db.commit()
        db.close()
