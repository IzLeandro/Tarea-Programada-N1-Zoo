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

#* Done; Al llamar utilizar la siguiente con entrada de cantidad, solicitar en el menu: leerTxtPrimeraVez(10)
#Lee todo el archivo
#!BUG
def leerTxtPrimeraVez(veces):
    listaFinal=[]
    nombreArchivo= input("Inserte el nombre del archivo con los animales: ")
    try:
        referencia = open((nombreArchivo),"r",encoding="utf8")
        leerLista = referencia.readlines()
        if veces>len(leerLista):
            print("El archivo cargado tiene menos animales de los que usted solicita, el maximo para ese archivo es de",len(leerLista))
            return
        while veces!=0:
            animal=leerLista[random.randrange(len(leerLista))]
            if animal not in listaFinal:
                listaFinal+= [animal] 
                veces-=1
                referencia.close()
                return borrarResiduosDelArchivo(listaFinal)
    except:
        return None

def borrarResiduosDelArchivo(listaAnimales):
    listaFinal=[]
    for i in listaAnimales:
        listaFinal+=[i[:-1]]
    return listaFinal

def grabarXml(nomArchGrabar,lista):
    """
    Funcion:Guarda el archivo 
    Entrada:El nombre del archivo y la lista con los elementos
    Salida:nada o un mensaje de error
    """
    nomArchGrabar+=".xml"
    try:
        f=open(nomArchGrabar,"w")
        f.writelines("<Zoologico>\n")
        for i in lista:
            f.writelines("\t<Animal>"+i[0]+"</Animal>\n")
            f.writelines("\t\t<Titulo>"+i[1]+"</Titulo>\n")
            f.writelines("\t\t<Url>"+i[2]+"</Url>\n")
            f.writelines("\t\t<Descript>"+i[3]+"</Descript>\n")
            f.writelines("\t\t<img>"+i[4]+"</img>\n")
            f.writelines("\t\t<Anotaciones>"+i[5]+"</Anotaciones>\n")
        f.writelines("</Zoologico>\n")
        f.close()
        print("¡Archivo xml creado correctamente!")
        return ""
    except:
        print("Ha ocurrido un error al crear el archivo xml.")