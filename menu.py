from files import cargarListaOriginal, readTxtFirstTime, grabar
archivo=input("Inserte el directorio donde se encuentra el archivo o si se encuentra en la misma carpeta, el nombre: ")
animales=cargarListaOriginal(archivo)
if animales==[]:
    print("ENTRAAAAAAAAAAAAAAAAAA")
    cantAnimales=eval(input("digite la cantidad de animales que desea obtener del archivo: "))
    animales= readTxtFirstTime(cantAnimales)


#!AL cerrar archivo o al abrir el archivo; guardar
grabar(archivo,animales)