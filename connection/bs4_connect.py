from bs4 import BeautifulSoup
import requests

def connect(link):
    result = requests.get(link)
    doc = BeautifulSoup(result.text, "html.parser")
    return doc

