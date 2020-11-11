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
def menu():
    global animales
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
    while True:
        print("""   
                         __  
                        /_/  
  _ __ ___   ___ _ __  _   _ 
 | '_ ` _ \ / _ \ '_ \| | | |
 | | | | | |  __/ | | | |_| |
 |_| |_| |_|\___|_| |_|\__,_|
                            """)
        print("1. Agregar animales")
        print("2. Obtener información de un animal")
        print("3. Registrar anotaciones")
        print("4. Apartar animales de mi zoológico")
        print("5. Salvaguardando estable mi zoológico")
        print("6. Exportando la base de datos")
        print("7. Salir del sistema de información")
        opcion = int(input("Digite una opción:"))
        if opcion == 1:
            cargaLista()
        elif opcion == 2:
            obtenerInformacion()
        elif opcion == 3:
            registrarAnotaciones()
        elif opcion == 4:
            apartarAnimales(numApartarAnimales())
        elif opcion == 5:
            salvaguardandoZoologico()   
        elif opcion == 6:
            nombreBase=input('Digite el nombre que sea ponerle al archivo: ')
            grabarXml(nombreBase,animales)
        elif opcion == 7:
            frases=["Una vez que una especie se extingue ninguna ley puede hacerla regresar: se ha marchado para siempre",
                    'Las mentes más profundas de todos los tiempos han sentido compasión por los animales',
                    'Si un hombre aspira a una vida correcta, su primer acto de abstinencia es el de lastimar animales',
                    'Podemos juzgar el corazón de una persona por la forma en que trata a los animales',
                    'Cuando un hombre se apiade de todas las criaturas vivientes, sólo entonces será noble' ]
            print(random.choice(frases))
            break
        else:
            print('Opción no válida')


#!EJECUCIÓN
#cargaLista()
#print(animales)
#menu()
#grabar(archivo,animales)
menu()

