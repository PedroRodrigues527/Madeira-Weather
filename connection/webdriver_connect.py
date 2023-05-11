from bs4 import BeautifulSoup
from selenium import webdriver
from utils.clean_screen import clean

def webdriverConnect(link):
    
    driver = webdriver.Firefox()
    driver.get(link)

    clean()
    print("Loading...")
    driver.implicitly_wait(10)
    clean()

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    driver.quit()
    
    return soup
