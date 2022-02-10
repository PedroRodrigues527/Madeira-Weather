import requests
import datetime
from bs4 import BeautifulSoup

#Get today time
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

def init():
    print("***METEOROLOGIA***")
    print("1- ATUAL")
    print("2- AMANHA")
    print("")
    op = input("")
    
    if op == '1':
        atualtemp()
    elif op == '2':
        print("AMANHA")
    else:   
        print("TENTE NOVAMENTE")
        init()

init()
