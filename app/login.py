from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from config import set_chrome_options
from readcsv import get_data
print("Selenium Version: "+str(webdriver.__version__))
def aestudiar(user: str, pasw: str):
    URL = "http://www.aestudiar.cl"
    domain = "aestudiar.cl"
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1024, 768)
    driver.get(URL)
    if not os.path.exists(domain):
        os.makedirs(domain)
    try:
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "yourUsername")))
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "yourPassword")))
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/section/div/div/div/div[2]/div/form/div[3]/button")))
        driver.save_screenshot(domain+"/1_page.png")
        username.click()
        username.send_keys(user)
        password.click()
        password.send_keys(pasw)
        driver.save_screenshot(domain+"/2_input.png")
        login_button.click()
        time.sleep(2)
        driver.save_screenshot(domain+"/3_response.png")
        
    finally:
        driver.close()
def educarex(user: str, pasw: str):
    URL = "https://radioedu.educarex.es/radiotomate/wp-login.php?loggedout=true&wp_lang=es_ES"
    domain = "radioedu.educarex.es"
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1024, 768)
    driver.get(URL)
    if not os.path.exists(domain):
        os.makedirs(domain)
    try:
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_login")))
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_pass")))
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wp-submit")))
        driver.save_screenshot(domain+"/1_"+user+".png")
        username.click()
        username.send_keys(user)
        password.click()
        password.send_keys(pasw)
        driver.save_screenshot(domain+"/2_"+user+".png")
        login_button.click()
        time.sleep(2)
        driver.save_screenshot(domain+"/3_"+user+".png")
    finally:
        driver.close()

aestudiar("hola","sdfsdf123")

for user in get_data():
    educarex(user[0],user[1])