#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 31/10/2020 2:40pm 
#Fecha de última Modificación: XX/XX/XX X:XXpm
#Versión: 3.9.0

#Importaciones
from IntegrationWikipedia import getInfo
import random
import time
#Definición de funciones
def cargarInfoWiki(animales):
    """
    Función:Imprime la información del animal seleccionado
    Entrada:el número del animal 
    Salida:la información del animal o un mensaje de error
    """
    lista=[]
    cont=0
    print("Obteniendo información desde Wikipedia...")
    for i in animales:
        print("Animales cargados: ",cont,"de",len(animales),end="\r")
        lista+=[getInfo(i)]
        cont+=1
    print("Información cargada correctamente.")
    time.sleep(2)
    return lista
    
def apartarAnimales(num,animales):
    """
    Función:Aparta la cantidad de animales escogida
    Entrada:el número de animales a apartar y la lista de animales
    Salida:la lista con los animales restantes
    """
    listaNueva=[]
    while num!=0:
        num-=1
        listaNueva.append(random.choice(animales))
    animales=listaNueva
    return animales

def registrarAnotaciones(matriz):
    """
    Función:Hace anotaciones en los animales
    Entrada:matriz
    Salida:la matriz con las anotaciones
    """
    while True:
        for i in range(len(matriz)):
            print(i+1,":",matriz[i][0])
        eleccion=input("Ingrese el número que represente al animal que desea agregar la anotación: ")
        try: eleccion=eval(eleccion)
        except: 
            print("Ingrese un valor correcto.") 
            time.sleep(2)
            continue
        if type(eleccion)!=int or eleccion<1 or eleccion>len(matriz):
            print("Ingrese un valor correcto.")
            time.sleep(2)
            continue
        anotacion=input("Dijite la anotación que desea agregar: ")
        matriz[eleccion-1][5]+=[anotacion]
        if not siNo():
            break
    return matriz

def siNo():
    """
    Función:pregunta si se desea realizar otra anotación
    Entrada: si o no 
    Salida:booleano o mensaje de error
    """
    entrada=input("Anotación agregada, desea agregar otra? SI/NO: ")
    if entrada.upper() == "SI":
        return True
    if entrada.upper() == "NO":
        return False
    else:
        print("Solo DEBE ingresar Si o No.")
        return siNo()

def salvaguardandoZoologico(matriz):
    """
    Función:Por cada animal en la lista simple agrega el animal a la matriz con todos sus datos, menos la imagen
    Entrada: matriz
    Salida:los datos de la matriz
    """
    for i in matriz:
        del i[4]
    for i in matriz:
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print(i[1],"Usualmente conocido como",i[0],"\n")
        print(i[3],"\n")
        if i[4]==[]:
            i[4]="No existen anotaciones y/o observaciones."
        print("Observaciones y anotaciònes: ",  i[4],"\n")
        print("Puedes encontrar màs informaciòn aquì:",i[2],"\n\n")
    return ""

def sacaListaAnimales(listaWiki):
    nuevaLista=[]
    for i in listaWiki:
        print(i)
        nuevaLista=i[0]
    return nuevaLista