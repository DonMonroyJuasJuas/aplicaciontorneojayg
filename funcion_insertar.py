import mysql.connector
from funcion_conexion import *

def insertar_variables_registro(fn,ap,em,pas):
    print("estamos en la funcion insertar usuarios")
    
    try:
            connection=conexion()
            if (connection):
                print("conexion realizada")

            Cursor=connection.cursor() 
            query="""INSERT INTO `registrar` (`Nombre`, `Apellido`, `Email`, `Password`) 
                                      VALUES (%s,%s ,%s ,%s )"""
            variable=(fn,ap,em,pas)
            Cursor.execute(query,variable)
 
            connection.commit()
            print("se ha realizado la insercion")
            return("la insercion se ha realizado señor usuario ")

    except mysql.connect.Error:
          print("failed to insert")
