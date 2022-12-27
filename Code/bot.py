from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import serial

import info
import time

arduino = serial.Serial(info.port, 9600, timeout=.1)
driver = webdriver.Chrome(info.PATH)
driver.get(info.link)
print("Connected!")

while True:
    # find add to cart button
    try:
        time.sleep(3)
        atcBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button")))
    except:
        driver.refresh()
        print("Refreshing...")
        continue

    print("GPU restocked!")
    # set off alarm
    try:
        arduino.write(b'Y')
        time.sleep(600)
    except Exception as e:
        continue
