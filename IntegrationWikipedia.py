import wikipedia
import re
import os
#?Listo
wikipedia.set_lang("ES")
def getInfo(animal):
    """
    Función:Obtiene desde wikipedia la informaciòn del animal
    Entrada:nombre del animal
    Salida:lista con info obtenida desde wiki
    """
    x=wikipedia.page(animal)
    info=[animal, x.title,x.url,cleanText(wikipedia.summary(animal)),x.images[0],[]]
    return info
def cleanText(texto):
    """
    Función:borra los caracteres que dificultan la lectura, especificamente el \u200b
    Entrada: texto 
    Salida: texto limpio
    """
    texto=cleanTextAux(texto)
    save=""
    for i in range(len(texto)):
        save=save+texto[i]
    save=save.replace("\u200b","")
    return save

def cleanTextAux(texto):
    """
    Función:borra los caracteres que dificultan la lectura, especificamente los [#]
    Entrada: texto 
    Salida: texto limpio
    """
    texto=str(texto)
    texto = re.sub("[[][\d][]]", " ", texto)
    texto = re.sub("[[][\d][\d][]]", " ", texto)
    os.system("cls")
    return texto