import mysql.connector

def conexion():
    connection = mysql.connector.connect(host='localhost',
                                             database='registrar',
                                             user='root',
                                             password='')
    print("funcion conexion")                                         
    return connection