import wikipedia
wikipedia.set_lang("ES")
def sacarInfo(nombre):
    x=wikipedia.page(nombre)
    info=[nombre, x.title,x.url,limpiarTexto(wikipedia.summary(nombre)),"image can be found here: " + x.images[0]]
    print(info)
    return ""

def limpiarTexto(texto):
    save=""
    flag=0
    for i in range(len(texto)):
        if flag!=0:
            flag-=1
            continue
        if texto[i]=="[": 
            flag=2
            continue
        save=save+texto[i]
    return save
  
sacarInfo("Oso Panda")