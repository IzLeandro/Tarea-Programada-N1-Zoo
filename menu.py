#Importaciones
from files import cargarListaOriginal, leerTxtPrimeraVez, grabar
from IntegrationWikipedia import getInfo
from function import cargarInfoWiki, apartarAnimales
import re
import random
#TODO:
#!AL cerrar archivo o al abrir el archivo; guardar
#!CADA VEZ QUE SE AGREGUE UN ANIMAL O SE BORRE UN ANIMAL SOBREESCRIBIR LA LISTA CON INFO DE WIKI
#? Ejemplo al abrir: C:\Users\ljafe\Desktop\prueba
#Variables Globales
archivo = ""
animales = []
animalesWiki = []
#Funciones
def cargaLista():
    global animales
    if animales == []:
        cantAnimales = input("Digite la cantidad de animales que desea obtener del archivo: ")
        if not re.match("^\d{1,}$",cantAnimales):
            print("Dijite únicamente numeros.")
            cargaLista()
            return''
        cantAnimales=eval(cantAnimales)
        animales = leerTxtPrimeraVez(cantAnimales)
    else:
        siNo=input("Se ha encontrado un archivo binario que contiene animales, desea cargarlo? SI/NO: ")
        if siNo.upper() == "SI":
            return 
        if siNo.upper() == "NO":
            animales=[]
            cargaLista()
        else:
            print("Solo DEBE ingresar Si o No.")
            cargaLista()
    return animales

def numApartarAnimales():
    global animales,animalesWiki
    numAnimales = input("Digite la cantidad de animales que es posible atender: ")
    while not re.match("^\d{1,}$",numAnimales):
        print("Dijite únicamente números.")
        numAnimales = input("Digite la cantidad de animales que es posible atender: ")   
    numAnimales=eval(numAnimales)
    print("Se han apartado: ",len(animales)-numAnimales,"del zoológico.")
    animales=apartarAnimales(numAnimales,animales)
    animalesWiki=cargarInfoWiki(animales)
    return ""

def obtenerInformacion():
    global animales,animalesWiki
    for i in range(len(animales)):
        print(i+1,":",animales[i])
    eleccion=eval(input("Ingrese el número de animal del que desea obtener información: "))
    if type(eleccion)!=int or eleccion<1 or eleccion>len(animales):
        print("Ingrese un valor correcto.")
        return ""
    print("A: ",animalesWiki[eleccion-1][1])
    print("B: ",animalesWiki[eleccion-1][2])
    print("C: ",animalesWiki[eleccion-1][3])
    print("D: ",animalesWiki[eleccion-1][4])
    return ""


#menu


#!EJECUCIÓN
archivo = input("Inserte el directorio donde se encuentra el archivo binario almacenado: ")
animales = cargarListaOriginal(archivo)
cargaLista()
animalesWiki = cargarInfoWiki(animales)
grabar(archivo,animales)

