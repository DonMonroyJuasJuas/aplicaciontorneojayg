from sqlite3 import Cursor
from funcion_conexion import * 

def funcionlogin(logemail):

    connection=conexion()
    cursor=connection.cursor()

    queryselect=("""SELECT Email, password from 
                   registrar where Email = %s""")
            
    
    cursor.execute(queryselect, (logemail,))
    myresult=cursor.fetchall()
    connection.commit()
    return myresult


