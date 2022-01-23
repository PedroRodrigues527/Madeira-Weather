import requests
import datetime
from bs4 import BeautifulSoup

#Read from internet
#Get info from URL
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


"""
#***TEMPO LISBOA***
url = 'https://weather.com/pt-PT/clima/hoje/l/POXX0016:1:PO?Goto=Redirected'

tempBox = doc.find("div", {"class": "CurrentConditions--CurrentConditions--1swR9"})
#print(tempBox.prettify())

tempValue = tempBox.find("span", {"class":"CurrentConditions--tempValue--3a50n"})
tempPlace = tempBox.find("h1", {"class":"CurrentConditions--location--kyTeL"})

print(tempPlace.string + ": " + tempValue.string)
"""
