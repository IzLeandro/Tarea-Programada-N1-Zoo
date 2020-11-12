#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 31/10/2020 2:32pm 
#Fecha de última Modificación: XX/XX/XX X:XXpm
#Versión: 3.9.0
#Importaciones 
from files import cargarListaOriginal, leerTxtPrimeraVez, grabar, grabarXml
from IntegrationWikipedia import getInfo
from function import cargarInfoWiki, apartarAnimales, registrarAnotaciones,salvaguardandoZoologico,sacaListaAnimales
import re, random, time, os
#? Ejemplo al abrir: C:\Users\ljafe\Desktop\prueba
#Variables Globales
flagPrimeraVez=True
animales = []
animalesWiki = []
nombreZoo=input("¡Bienvenido!\nDijite un nombre para su zoológico: ")
#Funciones
def cargaLista():
    """
    Función:Carga lista primera vez, y hace la funciòn de cargar el archivo binario las demàs
    Entrada:el número del animal 
    Salida:la información del animal o un mensaje de error
    """
    global animales,archivo,flagPrimeraVez,animalesWiki
    if flagPrimeraVez:
        cantAnimales = eval(input("Digite la cantidad de animales que desea obtener del archivo: "))
        if type(cantAnimales) != int:
            print("Debe digitar un nùmero entero.")
            return cargaLista()
        animales=leerTxtPrimeraVez(cantAnimales)
        flagPrimeraVez=False
        return ""
    siNo=input(" Desea cargar datos de un archivo previo?. SI/NO: ")
    if siNo.upper() == "SI":
        archivo = input("Inserte el directorio donde se encuentra el archivo binario almacenado: ")
        animalesWiki = cargarListaOriginal(archivo)
        animales = sacaListaAnimales(animalesWiki)
        print("Se ha cargado el archivo.")
        return ""
    if siNo.upper() == "NO":
        animales=[]
        flagPrimeraVez=True
        cargaLista()
        return ""
    else:
        print("Solo DEBE ingresar Si o No.")
        cargaLista()
    return ""

def numApartarAnimales():
    """
    Función: Revisa que el número digitado por el usuario esté bien y llama a la función apartarAnimales
    Entrada:el número de animales que se pueden atender  
    Salida:el mensaje de cuantos animales se apartaron 
    """
    global animales,animalesWiki
    numAnimales = input("Digite la cantidad de animales que es posible atender: ")
    while not re.match("^\d{1,}$",numAnimales):
        print("Dijite únicamente números.")
        numAnimales = input("Digite la cantidad de animales que es posible atender: ")   
    numAnimales=eval(numAnimales)
    while numAnimales>len(animales):
        print('Cantidad de animales mayor a la existente en el zoológico')
        numAnimales = input("Digite la cantidad de animales que es posible atender: ")
        while not re.match("^\d{1,}$",numAnimales):
            print("Dijite únicamente números.")
            numAnimales = input("Digite la cantidad de animales que es posible atender: ")  
        numAnimales=eval(numAnimales) 
    if len(animales)-numAnimales==1:
        print("Se ha apartado",len(animales)-numAnimales,"animal del zoológico.")
    else:
        print("Se han apartado",len(animales)-numAnimales,"animales del zoológico.")
    animales=apartarAnimales(numAnimales,animales)
    animalesWiki=cargarInfoWiki(animales)
    return ""

def obtenerInformacion():
    """
    Función:Imprime la información del animal seleccionado
    Entrada:el número del animal 
    Salida:la información del animal o un mensaje de error
    """
    global animales,animalesWiki
    for i in range(len(animales)):
        print(i+1,":",animales[i])
    eleccion=eval(input("Ingrese el número de animal del que desea obtener información: "))
    if type(eleccion)!=int or eleccion<1 or eleccion>len(animales):
        print("Ingrese un valor correcto.")
        return ""
    print()
    print("A.Título: ",animalesWiki[eleccion-1][1])
    print()
    print("B.URL de Wikipedia : ",animalesWiki[eleccion-1][2])
    print()
    print("C.Resumen del contenido: ",animalesWiki[eleccion-1][3])
    print()
    print("D.Imagen: ",animalesWiki[eleccion-1][4])
    return ""
#menu
def menu():
    """
    Función:Inicializa el menu
    Entrada:N/A
    Salida:N/A
    """
    global animales, animalesWiki
    print("""
                      ______           _   __        _            
                     |___  /          | | /_/       (_)                  
                        / / ___   ___ | | ___   __ _ _  ___ ___   
                       / / / _ \ / _ \| |/ _ \ / _` | |/ __/ _ \  
                      / /_| (_) | (_) | | (_) | (_| | | (_| (_) | 
                     /_____\___/ \___/|_|\___/ \__, |_|\___\___/                                                                             
                                                __/ |             
                                               |___/                         


                                        __,__
                               .--.  .-"     "-.  .--.
                              ' .. \/  .-. .-.  \/ .. '
                             | |  '|  /   Y   \  |'  | |
                             | \   \  \ 0 | 0 /  /   / |
                              \ '- ,\.-"`` ``"-./, -' /
                               `'-' /_   ^ ^   _\ '-'`
                                   |  \._   _./  |
                                   \   \ `~` /   /
                                    '._ '-=-' _.'
                                       '~---~'
    """)
    time.sleep(2)
    while True:
        time.sleep(1)
        print("""        
                         __  
                        /_/  
  _ __ ___   ___ _ __  _   _ 
 | '_ ` _ \ / _ \ '_ \| | | |
 | | | | | |  __/ | | | |_| |
 |_| |_| |_|\___|_| |_|\__,_|
                            """)
        print("   🦜",nombreZoo,"🦜   ")
        print("1. Agregar animales")
        print("2. Obtener información de un animal")
        print("3. Registrar anotaciones")
        print("4. Apartar animales de mi zoológico")
        print("5. Salvaguardando estable mi zoológico")
        print("6. Exportando la base de datos")
        print("7. Salir del sistema de información\n")
        opcion = input("Digite una opción: ")
        if opcion == '1':
            cargaLista()
        elif opcion == '2':
            obtenerInformacion()
            print()
            input('Digite enter para continuar...')
        elif opcion == '3':
            animalesWiki=registrarAnotaciones(animalesWiki)
            print("")
        elif opcion == '4':
            print()
            print('----Apartar animales de mi zoológico----')
            print()
            numApartarAnimales()
            print()
            input('Digite enter para continuar...')
        elif opcion == '5':
            salvaguardandoZoologico(animalesWiki) 
        elif opcion == '6':
            print()
            print('----Exportando la base de datos----')
            print()
            nombreBase=input('Digite el nombre que sea ponerle al archivo: ')
            grabarXml(nombreBase,animalesWiki)
            input('Digite enter para continuar...')
        elif opcion == '7':
            siNo=input(" Desea guardar su informaciòn en un archivo binario?. SI/NO: ")
            if siNo.upper() == "SI":
                grabar(animalesWiki)
                print("Se ha guardado el archivo.")
            print()
            print('Saliendo del sistema de información...')
            print()
            frases=["Una vez que una especie se extingue ninguna ley puede hacerla regresar: se ha marchado para siempre",
                    'Las mentes más profundas de todos los tiempos han sentido compasión por los animales',
                    'Si un hombre aspira a una vida correcta, su primer acto de abstinencia es el de lastimar animales',
                    'Podemos juzgar el corazón de una persona por la forma en que trata a los animales',
                    'Cuando un hombre se apiade de todas las criaturas vivientes, sólo entonces será noble']
            time.sleep(2)
            print(random.choice(frases))
            break
        else:
            print()
            print('Opción no válida')
            print()
            input('Digite enter para continuar...')
#menu
#!EJECUCIÓN
cargaLista()
animalesWiki = cargarInfoWiki(animales)
menu()

