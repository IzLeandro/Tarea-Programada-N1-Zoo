from IntegrationWikipedia import getInfo
import random
import time
def cargarInfoWiki(animales):
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
    listaNueva=[]
    while num!=0:
        num-=1
        listaNueva.append(random.choice(animales))
    animales=listaNueva
    return animales

def registrarAnotaciones(matriz):
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
    entrada=input("Anotaciòn Agregada, desea agregar otra? SI/NO: ")
    if entrada.upper() == "SI":
        return True
    if entrada.upper() == "NO":
        return False
    else:
        print("Solo DEBE ingresar Si o No.")
        return siNo()

def salvaguardandoZoologico(matriz):
    for i in matriz:
        del i[4]
    print(matriz)
    for i in matriz:
        #print(i)
        print(i[1],"Usualmente conocido como",i[0],"\n")
        print(i[3],"\n")
        if i[4]==[]:
            i[4]="No existen anotaciones y/o observaciones."
        print("Observaciones y anotaciònes: ",  i[4],"\n")
        print("Puedes encontrar màs informaciòn aquì:",i[2],"\n\n")
    return ""