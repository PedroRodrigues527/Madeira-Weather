"""
Author: Pedro Rodrigues;
Description: Retrieve weather information about Madeira 
             Island using python (Webscraping);
2022
"""


import requests
import datetime
from bs4 import BeautifulSoup

#Get today weather
def atualtemp():
    #Read from internet
    #Get info from URL
    print("*** TEMPO ATUAL ***")
    url = 'https://www.tempo.pt/madeira-provincia.htm'
    result = requests.get(url) #GET request
    #print(result.text)
    
    doc = BeautifulSoup(result.text, "html.parser")
    #print(doc.prettify())
    
    #Tempo madeira
    tempBox = doc.find("ul", {"class":"ul-top-prediccion top-pred"})
    tempPredict = tempBox.find_all("li", {"class":"li-top-prediccion"})
    
    today = datetime.datetime.now()
    print (today.strftime("%Y-%m-%d %H:%M:%S"))
    
    for temperatura in tempPredict:
        lugar = temperatura.find("a", {"class":"anchors"})
        maxTemp = temperatura.find("span", {"class": "cMax changeUnitT"})
        minTemp = temperatura.find("span", {"class": "cMin changeUnitT"})
        print(str(lugar.string) + " Max: " + str(maxTemp.string) + " Min: " + str(minTemp.string))
    print("")
    init()

#Get all week information
def amanhaTemp():
    #Read from internet
    #Get info from URL
    print("*** TEMPO ATE 7 DIAS ***")
    url = ['https://www.tempo.pt/calheta.htm','https://www.tempo.pt/camara-de-lobos.htm','https://www.tempo.pt/funchal.htm','https://www.tempo.pt/machico.htm','https://www.tempo.pt/ponta-do-sol.htm','https://www.tempo.pt/porto-moniz.htm','https://www.tempo.pt/ribeira-brava.htm','https://www.tempo.pt/santa-cruz_madeira-l32099.htm','https://www.tempo.pt/santana.htm','https://www.tempo.pt/sao-vicente.htm']
    lugares = ["Calheta","Camara de Lobos","Funchal","Machico","Ponta de Sol","Porto Moniz","Ribeira Brava","Santa Cruz","Santana","São Vicente"]
    
    for i in range(len(url)):
        result = requests.get(url[i]) #GET request
        #print(result.text)
        #print(result)
        
        doc = BeautifulSoup(result.text, "html.parser")
        #print(doc.prettify())
        
        #Tempo madeira
        print(lugares[i])
        tempBox = doc.find("span", {"class":"datos-dos-semanas"})
        #tempSpan = tempBox.find("span",{"class":"datos-dos-semanas"})
        #tempPredict = tempSpan.find_all("li")
        #print(tempBox)
        
        
        liTemp = tempBox.find_all("li")
        
        i = 0 #control of week
        for li in liTemp:
            #semana = li.find("span", {"class": "cuando"})
            Temp = li.find("span", {"class": "temperatura"})
            maxTemp = Temp.find("span", {"class": "maxima changeUnitT"})
            minTemp = Temp.find("span", {"class": "minima changeUnitT"})
            print("Dia "+str(i)+" "+str(maxTemp.string)+""+str(minTemp.string))
            i+=1
            if i == 7:
                print("")
                break
    print("")
    init()    

def init():
    print("***METEOROLOGIA***")
    print("1- ATUAL")
    print("2- HOJE ATE 7 DIAS")
    print("")
    op = input("")
    
    if op == '1':
        atualtemp()
    elif op == '2':
        amanhaTemp()
    else:   
        print("TENTE NOVAMENTE")
        init()

init()
