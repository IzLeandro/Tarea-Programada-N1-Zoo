from files import cargarListaOriginal, readTxtFirstTime, grabar
archivo = input("Inserte el directorio donde se encuentra el archivo o si se encuentra en la misma carpeta, el nombre: ")
animales = cargarListaOriginal(archivo)
print(archivo)
if animales == []:
    print("ENTRAAAAAAAAAAAAAAAAAA")
    cantAnimales = eval(input("digite la cantidad de animales que desea obtener del archivo: "))
    animales = readTxtFirstTime(cantAnimales)
    #* re.match("^\d{1,}$",num) falta comprobar con 0
else:
    print(animales)
    print("entra abajo")
#C:\Users\ljafe\Desktop\prueba
#!AL cerrar archivo o al abrir el archivo; guardar
grabar(archivo, animales)
