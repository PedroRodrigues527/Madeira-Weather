"""
Author: Pedro Rodrigues;
Description: Retrieve weather information about Madeira 
             Island using python (Webscraping);
2022
"""

import requests
import datetime
from os import system, name
from bs4 import BeautifulSoup

url = ['https://www.tempo.pt/calheta.htm','https://www.tempo.pt/camara-de-lobos.htm','https://www.tempo.pt/funchal.htm','https://www.tempo.pt/machico.htm','https://www.tempo.pt/ponta-do-sol.htm','https://www.tempo.pt/porto-moniz.htm','https://www.tempo.pt/ribeira-brava.htm','https://www.tempo.pt/santa-cruz_madeira-l32099.htm','https://www.tempo.pt/santana.htm','https://www.tempo.pt/sao-vicente.htm']

lugares = ["Calheta","Camara de Lobos","Funchal","Machico","Ponta de Sol","Porto Moniz","Ribeira Brava","Santa Cruz","Santana","São Vicente"]

def places():
    clean()
    print("***ESPECIFICO***")
    index = 1
    for lugar in range(len(lugares)-1):
        print(str(index) + "- "+ lugares[lugar])
        index += 1
    op = input("")
    
    #ATUAL DE LUGAR
    try:
        print("");
        print("Info: "+ lugares[int(op)-1])
        atualtempEsp(lugares[int(op)-1])
    except:
        print("Utilize opção correta e apenas caracteres numericos")
        
def atualtempEsp(lugarStr):
    tempBox = connect('https://www.tempo.pt/madeira-provincia.htm').find("ul", {"class":"ul-top-prediccion top-pred"})
    tempPredict = tempBox.find_all("li", {"class":"li-top-prediccion"})  
    time()
    for temperatura in tempPredict:
        lugar = temperatura.find("a", {"class":"anchors"})
        if lugarStr == str(temperatura.find("a", {"class":"anchors"}).string):
            maxTemp = temperatura.find("span", {"class": "cMax changeUnitT"})
            minTemp = temperatura.find("span", {"class": "cMin changeUnitT"})
            print(str(lugar.string) + " Max: " + str(maxTemp.string) + " Min: " + str(minTemp.string))
    print("")
    init()

def connect(link):
    url = link
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    return doc

def atualtemp():
    tempBox = connect('https://www.tempo.pt/madeira-provincia.htm').find("ul", {"class":"ul-top-prediccion top-pred"})
    tempPredict = tempBox.find_all("li", {"class":"li-top-prediccion"})
    
    time()
    text = [];
    for temperatura in tempPredict:
        lugar = temperatura.find("a", {"class":"anchors"})
        maxTemp = temperatura.find("span", {"class": "cMax changeUnitT"})
        minTemp = temperatura.find("span", {"class": "cMin changeUnitT"})
        print(str(lugar.string) + " Max: " + str(maxTemp.string) + " Min: " + str(minTemp.string))
        textStr = str(lugar.string) + " Max: " + str(maxTemp.string) + " Min: " + str(minTemp.string) + "\n";
        text.append(textStr)
    print("")
    saveToFile(text, "weatherAtual.txt")
    init()

def amanhaTemp():
    print("*** TEMPO ATE 7 DIAS ***")
    text = [];
    for i in range(len(url)):
        print(lugares[i])
        text.append("****\n"+lugares[i]+"\n")
        tempBox = connect(url[i]).find("span", {"class":"datos-dos-semanas"})
        liTemp = tempBox.find_all("li")  
        i = 0 #control of week
        #text = [];
        for li in liTemp:
            dia = li.find("span",{"class": "cuando"})
            
            Temp = li.find("span", {"class": "temperatura"})
            maxTemp = Temp.find("span", {"class": "maxima changeUnitT"})
            minTemp = Temp.find("span", {"class": "minima changeUnitT"})
            print(str(dia.text)+" Max:"+str(maxTemp.string)+" Min:"+str(minTemp.string))
            textStr = str(dia.text)+" Max:"+str(maxTemp.string)+" Min:"+str(minTemp.string) + "\n"
            text.append(textStr)
            i+=1
            if i == 7:
                text.append("\n")
                print("")
                break
        saveToFile(text, "weatherWeek.txt")
    print("")
    init()    
    
def saveToFile(content, file):
    try:
        with open(file, 'w') as f:
            for strings in content:
                f.write(strings)
                #f.write("\n")
            print("Content saved with success")    
    except:
        print("Erro has occurred aborting!")
        
        
#cleaning console
def clean():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def time():
    today = datetime.datetime.now()
    print (today.strftime("%Y-%m-%d %H:%M:%S"))


def init():
    print("***METEOROLOGIA***")
    print("1- ATUAL")
    print("2- HOJE ATE 7 DIAS")
    print("3- ESPECIFICO")
    print("")
    op = input("")
    
    try:
        if op == '1':     
            atualtemp()
        elif op == '2':  
            amanhaTemp()
        elif op == '3':
            places()    
    except:

        print("Option not valid\nUse only numerical caracters between 1 and 3")
        init()

if __name__=='__main__':
    init()
