#Importaciones
from files import cargarListaOriginal, leerTxtPrimeraVez, grabar
from IntegrationWikipedia import getInfo
import re
import random
#TODO:
#!AL cerrar archivo o al abrir el archivo; guardar
#? Ejemplo al abrir: C:\Users\ljafe\Desktop\prueba
#Variables Globales
archivo = input("Inserte el directorio donde se encuentra el archivo binario almacenado: ")
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
    numAnimales = input("Digite la cantidad de animales que es posible atender: ")
    while not re.match("^\d{1,}$",numAnimales):
        print("Dijite únicamente números.")
        numAnimales = input("Digite la cantidad de animales que es posible atender: ")   
    numAnimales=eval(numAnimales)
    return numAnimales

def apartarAnimales():
    num=numApartarAnimales()
    global animales
    listaNueva=[]
    while num!=0:
        num-=1
        listaNueva.append(random.choice(animales))
    animales=listaNueva
    return animales
def obtenerInformacion(animal):
    animal=getInfo(animal)
    print("A: ",animal[1])
    print("B: ",animal[2])
    print("C: ",animal[3])
    print("D: ",animal[4])
    return ""
#menu



#!EJECUCIÓN
#cargaLista()
#print(animales)
#menu()
#grabar(archivo,animales)
print(obtenerInformacion("sapo"))

