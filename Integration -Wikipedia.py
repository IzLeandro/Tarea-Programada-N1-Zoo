import wikipedia
wikipedia.set_lang("ES")
def getInfo(animal):
    x=wikipedia.page(animal)
    info=[animal, x.title,x.url,cleanText(wikipedia.summary(animal)),"La imagen puede ser encontrada aquí: " + x.images[0],""]
    print(info)
    return ""
def cleanText(text):
    save=""
    flag=0
    for i in range(len(text)):
        if flag!=0:
            flag-=1
            continue
        if text[i]=="[": 
            flag=3
            continue
        save=save+text[i]
    save=save.replace("\u200b","")
    return save