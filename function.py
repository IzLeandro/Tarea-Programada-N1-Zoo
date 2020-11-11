from IntegrationWikipedia import getInfo
import random

def cargarInfoWiki(animales):
    lista=[]
    cont=0
    print("Obteniendo información desde Wikipedia...")
    for i in animales:
        print("Animales cargados: ",cont,"de",len(animales),end="\r")
        lista.append(getInfo(i))
        cont+=1
    print("Información cargada correctamente.")
    return lista
    
def apartarAnimales(num,animales):
    listaNueva=[]
    while num!=0:
        num-=1
        listaNueva.append(random.choice(animales))
    animales=listaNueva
    return animales
    