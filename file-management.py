#imports
import random
import os
#! Al llamar utilizar la siguiente con entrada de cantidad, solicitar en el menu: readTxtFirstTime(10)
#Lee todo el archivo
def readTxtFirstTime(times):
    finalList=[]
    fileName= input("Inserte el nombre del archivo: ")
    reference = open((fileName),"r",encoding="utf8")
    readList = reference.readlines()
    while times!=0:
        animal=readList[random.randrange(len(readList))]
        if animal not in finalList:
            finalList+= [animal] 
            times-=1
    reference.close()
    return print(deleteResidueFromFile(finalList))
def deleteResidueFromFile(listAnimals):
    finalList=[]
    for i in listAnimals:
        finalList+=[i[:-1]]
    return finalList

readTxtFirstTime(10)