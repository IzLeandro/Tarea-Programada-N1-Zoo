import wikipedia
import re
import os
#?Listo
wikipedia.set_lang("ES")
def getInfo(animal):
    x=wikipedia.page(animal)
    info=[animal, x.title,x.url,cleanText(wikipedia.summary(animal)),x.images[0],[]]
    return info
def cleanText(texto):
    texto=cleanTextAux(texto)
    save=""
    for i in range(len(texto)):
        save=save+texto[i]
    save=save.replace("\u200b","")
    return save

def cleanTextAux(texto):
    texto=str(texto)
    texto = re.sub("[[][\d][]]", " ", texto)
    texto = re.sub("[[][\d][\d][]]", " ", texto)
    os.system("cls")
    return texto