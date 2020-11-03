#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 31/10/2020 1:32pm 
#Fecha de última Modificación: XX/XX/XX X:XXpm
#Versión: 3.8.5
#Importación de librerias 
import pickle
#Variables globales
listaOriginal=['Loro Cabeza Amarilla', 'Águila Real', 'Jirafa Reticulada', 'Escorpión', 'Oso Polar']
bandera=0
#Funciones 
#! PARA COMPROBAR SI EL ARCHIVO EXISTE, REVISAR SI LISTA == []
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
    #!asdasdasd
def cargarListaOriginal(listaOriginal):
    """
    Funcion:Carga los donantes
    Entradas:la lista de donantes
    Salidas:NA
    """
    while True:
            try:
                listaOriginal = leer("listaOriginal")
                return listaOriginal
            except:
                grabar("listaOriginal",listaOriginal)
listaOriginal=cargarListaOriginal(listaOriginal)
print(listaOriginal)