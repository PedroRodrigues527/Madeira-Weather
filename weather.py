"""
Author: Pedro Rodrigues;
Description: Retrieve weather information about Madeira 
             Island using python (Webscraping);
2022
"""
from typing import List
import datetime
import yagmail
from connection.bs4_connect import connect
from connection.webdriver_connect import webdriverConnect
from utils.clean_screen import clean
from utils.save_file import saveToFile


url = ['https://www.tempo.pt/calheta.htm', 'https://www.tempo.pt/camara-de-lobos.htm',
       'https://www.tempo.pt/funchal.htm', 'https://www.tempo.pt/machico.htm', 'https://www.tempo.pt/ponta-do-sol.htm',
       'https://www.tempo.pt/porto-moniz.htm', 'https://www.tempo.pt/ribeira-brava.htm',
       'https://www.tempo.pt/santa-cruz_madeira-l32099.htm', 'https://www.tempo.pt/santana.htm',
       'https://www.tempo.pt/sao-vicente.htm']

lugares: list[str] = ["Calheta", "Camara de Lobos", "Funchal", "Machico", "Ponta de Sol", "Porto Moniz",
                      "Ribeira Brava", "Santa Cruz", "Santana", "São Vicente"]

def showLugares():
    for lugar in range(len(lugares) - 1):
        print(str(lugar) + "- " + lugares[lugar])

def places():
    clean()
    print("***ESPECIFICO***")
    showLugares()
    city = input("")

    try:
        print("")
        print("Info: " + lugares[int(city)])
        atualTempoEspecifico(lugares[int(city)])
    except IndexError:
        print("Utilize opção correta e apenas caracteres numericos")
        places()

def atualTempoEspecifico(place):
    tempBox = connect('https://www.tempo.pt/madeira-provincia.htm').find("ul", {"class": "ul-top-prediccion top-pred"})
    tempPredict = tempBox.find_all("li", {"class": "li-top-prediccion"})
    time()
    for temperatura in tempPredict:
        lugar = temperatura.find("a", {"class": "anchors"})
        if place == str(temperatura.find("a", {"class": "anchors"}).string):
            maxTemp = temperatura.find("span", {"class": "cMax changeUnitT"})
            minTemp = temperatura.find("span", {"class": "cMin changeUnitT"})
            display(str(lugar.string), str(maxTemp.string), str(minTemp.string))
    print("")
    init()

def display(lugar, max_temp, min_temp):
    global output
    output = lugar
    MAX_SIZE = 16
    MAX_SIZE_TEMPERATURE = 10
    if len(lugar) <= MAX_SIZE:
        for space in range(MAX_SIZE - len(lugar)):
            output = output + " "
    output = output + " Max: " + max_temp
    output = output + " Min: " + min_temp
    print(output)


def atualTempo():
    """ tempBox = connect('https://www.tempo.pt/madeira-provincia.htm').find("ul", {"class": "ul-top-prediccion top-pred"})
    tempPredict = tempBox.find_all("li", {"class": "li-top-prediccion"})
    time()
    
    for temperatura in tempPredict:
        lugar = temperatura.find("a", {"class": "anchors"})
        maxTemp = temperatura.find("span", {"class": "cMax changeUnitT"})
        minTemp = temperatura.find("span", {"class": "cMin changeUnitT"})
        display(str(lugar.string), str(maxTemp.string), str(minTemp.string))
        text.append(output) """

    """ tempBox = connect("https://www.tempo.pt/madeira-provincia.htm").find("section").find("div",{"id":"mapaNew"}) """

    connection = webdriverConnect('https://www.tempo.pt/madeira-provincia.htm')

    tempBox = connection.find("section").find("div", {"id": "mapaNew"}).find("div", {"class": "leaflet-pane leaflet-marker-pane"}).find_all("a")

    text = []
    for element in tempBox:
        location_name = element.find_all("span")[-1].text
        max_temperature = element.find("span",{"class": "red changeUnitT"}).text
        min_temperature = element.find("span",{"class": "blue changeUnitT"}).text

        display(str(location_name), str(max_temperature), str(min_temperature))
        text.append(output+"\n")

    saveToFile(text, "weather.txt")
    time()
    init()


def weekTempo():
    print("*** TEMPO ATE 7 DIAS ***")
    text = []
    for i in range(len(url)):
        try:
            print(lugares[i])
            text.append("****\n" + lugares[i] + "\n")
            tempBox = connect(url[i]).find("span", {"class": "datos-dos-semanas"})
            liTemp = tempBox.find_all("li")
            day_of_the_week = 0  # control of week
            for li in liTemp:
                dia = li.find("span", {"class": "cuando"})
                Temp = li.find("span", {"class": "temperatura"})
                maxTemp = Temp.find("span", {"class": "maxima changeUnitT"})
                minTemp = Temp.find("span", {"class": "minima changeUnitT"})

                MAX_SIZE_DAY = 15

                MAX_SIZE = 12
                letters = ""
                month = ""
                number = ""


                #Identify number and month from string
                for char in range(len(str(dia.text))):
                    if dia.text[char].isnumeric():
                        for size in range(MAX_SIZE_DAY - char):
                            number = str(dia.text[char])
                    elif str(dia.text[char]) == "J":
                        for size in range(MAX_SIZE_DAY - char):
                            month += " "
                        letters = letters + month + "J"
                    else:
                        letters = letters + str(dia.text[char])

                finalString = letters
                if len(letters) <= MAX_SIZE:
                    for space in range(MAX_SIZE - len(letters)):
                        finalString = finalString + " "
                finalString = finalString + number

                display(str(finalString), str(maxTemp.string), str(minTemp.string))
                text.append(output)
                day_of_the_week += 1
                if day_of_the_week == 7: #Fim da semana
                    text.append("\n")
                    print("")
                    break
            saveToFile(text, "weather.txt")
        except FileExistsError:
            print("Error saving to file!")
    print("")
    init()

def sendEmail():
    try:
        user_email = input("Insira o seu email: ")
        yag = yagmail.SMTP('xxx@gmail.com', 'xxx')
        yag.send(user_email, 'Weather Report', "Weather Report", 'weather.txt')
        print("Enviando por email...")
        print("Enviado")
    except ConnectionError as e:
        print("Error while sending the email.\n"+e)
    except ConnectionResetError as e:
        print("Error while connecting the email.\n" + e)
    except ConnectionAbortedError as e:
        print("Error connection aborted\n" + e)
    except ConnectionRefusedError as e:
        print("Error connection refused.\n" + e)

def time():
    today = datetime.datetime.now()
    print(today.strftime("%Y-%m-%d %H:%M:%S.%f"))

def showMainMenu():
    print("***METEOROLOGIA***")
    print("1- ATUAL")
    print("2- HOJE ATE 7 DIAS")
    print("3- ESPECIFICO")
    print("4- Enviar por email")
    print("")

def init():
    showMainMenu()
    op = input("")

    if op == '1':
        atualTempo()
    elif op == '2':
        weekTempo()
    elif op == '3':
        places()
    elif op == '4':
        sendEmail()
    else:
        print("Option not valid\nUse only numerical characters between 1 and 3")
        init()


if __name__ == '__main__':
    init() 
