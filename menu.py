#Importaciones
from files import cargarListaOriginal, readTxtFirstTime, grabar
import re
import random
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
        cantAnimales = input("Digite la cantidad de animales que desea obtener del archivo: ")
        if not re.match("^\d{1,}$",cantAnimales):
            print("Dijite únicamente numeros.")
            cargaLista()
            return''
        cantAnimales=eval(cantAnimales)
        animales = readTxtFirstTime(cantAnimales)
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
animales2=cargaLista()
def numApartarAnimales():
    numAnimales = input("Digite la cantidad de animales que es posible atender: ")
    while not re.match("^\d{1,}$",numAnimales):
        print("Dijite únicamente números.")
        numAnimales = input("Digite la cantidad de animales que es posible atender: ")   
    numAnimales=eval(numAnimales)
    return numAnimales

def apartarAnimales():
    num=numApartarAnimales()
    global animales2
    listaNueva=[]
    for i in range(num):
        listaNueva.append(random.choice(animales2))
    return listaNueva
#Corrida
#an=cargaLista()
#print(an)
#grabar(archivo, animales)

