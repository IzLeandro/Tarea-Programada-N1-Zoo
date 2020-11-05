#Importaciones
from files import cargarListaOriginal, leerTxtPrimeraVez, grabar
import re
#TODO:
#!AL cerrar archivo o al abrir el archivo; guardar
#? C:\Users\ljafe\Desktop\prueba
#Variables Globales
archivo = input("Inserte el directorio donde se encuentra el archivo o si se encuentra en la misma carpeta, el nombre: ")
animales = cargarListaOriginal(archivo)
#Funciones
def cargaLista():
    global animales
    if animales == []:
        cantAnimales = input("digite la cantidad de animales que desea obtener del archivo: ")
        if not re.match("^\d{1,}$",cantAnimales):
            print("Dijite unicamente numeros.")
            cargaLista()
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
#Corrida
cargaLista()
print(animales)
grabar(archivo, animales)
