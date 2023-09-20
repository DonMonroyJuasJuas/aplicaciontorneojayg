from multiprocessing import connection
from sqlite3 import Cursor
from uvicorn import *
from fastapi import *
from fastapi.templating import *
from fastapi.staticfiles import *
import mysql.connector
import uvicorn
from funcion_conexion import *
from funcion_insertar import *
from funcion_seleclogin import funcionlogin
templates = Jinja2Templates(directory="D:/servidorweb/static")
app=APIRouter()#crear na instancia de fastapi

#configurar la instancia de fastapi con el directorio 
app.mount("/static", StaticFiles(directory=r"D:\servidorweb\static"),name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("/index.html",{"request":request})

@app.post("/registrar")
def formularioregistrar(request: Request,fn: str = Form(...), ap: str = Form(...), em: str = Form(...), pas: str = Form(...) ):
    print(fn)
    print(ap)
    print(em) 
    print(pas)
    print("esta es la ruta registrarRR")
    insertar_variables_registro(fn,ap,em,pas)
    return templates.TemplateResponse("/html/iniciodesesion.html",{"request":request})
  
@app.post("/seleclogin")
def form_login(request: Request,logemail: str=Form(...) ,logpass:str=Form(...)):
    print(logemail)
    print(logpass)
    datos=funcionlogin(logemail)

    return datos
    print("RUTA SELEC LOGIN")


if __name__=='__main__':
    print("metodo principal aqui inicia la ejecucion")
    uvicorn.run(app,host="localhost", port=8081)
    