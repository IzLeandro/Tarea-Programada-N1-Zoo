#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 31/10/2020 1:32pm 
#Fecha de última Modificación: XX/XX/XX X:XXpm
#Versión: 3.8.5
#Importación de librerias 
import pickle
import random
import os
#Funciones 
#* Done: PARA COMPROBAR SI EL ARCHIVO EXISTE, REVISAR SI LISTA == []
def grabar(nomArchGrabar,lista):
    """
    Funcion:Grabar la lista en el archivo deseado
    Entrada:El nombre del archivo y la lista con los elementos
    Salida:nada o un mensaje de error
    """
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
def leer(nomArchLeer):
    """
    Funcion:Lee el archivo selecionado
    Entrada:El nombre del archivo
    Salida:NA
    """
    lista=[]
    f=open(nomArchLeer,"rb")
    lista = pickle.load(f)
    f.close()
    return lista
    #!Funcion que necesitamos
def cargarListaOriginal(archivo):
    """
    Funcion:Carga los donantes
    Entradas:la lista de donantes
    Salidas:NA
    """
    var=[]
    while True:
            try:
                var = leer(archivo)
                return var
            except:
                grabar(archivo,var)

#* Done; Al llamar utilizar la siguiente con entrada de cantidad, solicitar en el menu: readTxtFirstTime(10)
#Lee todo el archivo
def readTxtFirstTime(times):
    finalList=[]
    fileName= input("Inserte el nombre del archivo: ")
    reference = open((fileName),"r",encoding="utf8")
    readList = reference.readlines()
    while times!=0:
        animal=readList[random.randrange(len(readList))]
        if animal not in finalList:
            finalList+= [animal] 
            times-=1
    reference.close()
    return deleteResidueFromFile(finalList)
def deleteResidueFromFile(listAnimals):
    finalList=[]
    for i in listAnimals:
        finalList+=[i[:-1]]
    return finalList
