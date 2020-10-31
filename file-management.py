#imports
import random

#Lee todo el archivo
def readTxtFirstTime():
    nombreArchivo= input("Inserte el nombre del archivo")
    referencia = open(nombreArchivo,"r")
    print("->Imprime todo el archivo...")
    print(referencia)
    lista = referencia.readlines()
    print(lista[random.randrange(len(lista))])
    referencia.close()
    return ""