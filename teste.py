import time
import requests
import datetime
from bs4 import BeautifulSoup

while True:
  #Get total time (HH:MM)
  localtime = time.localtime()
  result = time.strftime("%H:%M", localtime)
  #print(result)#Time
  
  
  #Get hour and minutes
  hour = time.strftime("%H", localtime)
  minutes = time.strftime("%M", localtime)
  
  minutes = int(minutes)+1
  if minutes >= 60:
    hour = int(hour)+1
    minutes = 0
    if hour >= 24:
      hour = str(hour)
      hour = "00"
  hour = str(hour)
  minutes = str(minutes)
  nextTime = hour+ ":" + minutes
      
  print("Nextime: " + nextTime)
  
  
  if result == nextTime:
    #Executar report tempo!
    
    #Store time
    time = result
    
    #Text to be in report
    text = ""
    text += time + "\n"
    #print (time)        
    
    #Read from internet
    #Get info from URL
    url = 'https://www.tempo.pt/madeira-provincia.htm'
    result = requests.get(url) #GET request
    
    doc = BeautifulSoup(result.text, "html.parser")

    
    #Tempo madeira
    tempBox = doc.find("ul", {"class":"ul-top-prediccion top-pred"})
    tempPredict = tempBox.find_all("li", {"class":"li-top-prediccion"})    

    for temperatura in tempPredict:
        lugar = temperatura.find("a", {"class":"anchors"})
        maxTemp = temperatura.find("span", {"class": "cMax changeUnitT"})
        minTemp = temperatura.find("span", {"class": "cMin changeUnitT"})
        text += str(lugar.string) + " Max: " + str(maxTemp.string) + " Min: " + str(minTemp.string) + "\n"
    
    print(text)
    
    #To open local html file:
    with open("report.txt", "w") as f:
        f.write(text)
        print("Success report!")    
    
    print("tempoooo")
  #time.sleep(1)

"""
for temperatura in tempPredict:
    lugar = temperatura.find("a", {"class":"anchors"})
    maxTemp = temperatura.find("span", {"class": "cMax changeUnitT"})
    minTemp = temperatura.find("span", {"class": "cMin changeUnitT"})
    text += str(lugar.string) + " Max: " + str(maxTemp.string) + " Min: " + str(minTemp.string) + "\n"

print(text)

#To open local html file:
with open("report.txt", "w") as f:
    f.write(text)
    print("Success report!")

"""

