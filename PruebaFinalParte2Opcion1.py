import time
from unicodedata import name
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://localhost:8114/")
elem1 = driver.find_element(By.ID, "user")
elem1.clear()
elem1.send_keys("root")
elem2 = driver.find_element(By.NAME, "pass")
elem2.clear()
elem2.send_keys("password")
elem2.send_keys(Keys.ENTER)
driver.get("http://localhost:8114")
elem3=driver.find_element(By.NAME,"Subject")
elem3.clear
elem3.send_keys("Prueba final Intro DevOps")
elem4=driver.find_element(By.NAME,"Content")
elem4.clear
elem4.send_keys("Completo el contenido del ticket antes de enviar")
elem5=driver.find_element(By.NAME,"SubmitTicket")
elem5.click
time.sleep(30)