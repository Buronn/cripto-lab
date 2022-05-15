from generate_user import *
from tqdm import tqdm
from api_mail import generateEmail
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import set_chrome_options
import time
import os

def loginCL(email, pasw, driver,i):
    domain = "hito_iv/test_login_CL"
    if not os.path.exists(domain):
        os.makedirs(domain)
    try:
        input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
        input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/form/button")))
        input_email.click()
        input_email.send_keys(email)
        input_password.click()
        input_password.send_keys(pasw)
        submit_button.click()
        driver.save_screenshot(domain+"/"+str(i)+".png")
    except:
        print("CL: Login failed")
        driver.close()
def loginES(email, pasw,driver,i):
    domain = "hito_iv/test_login_ES"
    if not os.path.exists(domain):
        os.makedirs(domain)
    try:
        input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login-email/form/div/div[6]/button")))
        input_email.click()
        input_email.send_keys(email)
        input_password.click()
        input_password.send_keys(pasw)
        submit_button.click()
        driver.save_screenshot(domain+"/"+str(i)+".png")
        input_email.click()
        input_email.clear()
        input_password.click()
        input_password.clear()
    except:
        print("ES: Login failed")
        driver.close()


email = "d1pxdkmotii@1secmail.org"

driver1 = webdriver.Chrome(options=set_chrome_options())
driver1.set_window_size(1024, 768)
driver1.get("https://account.getagil.com/signin")
driver2 = webdriver.Chrome(options=set_chrome_options())
driver2.set_window_size(1024, 768)
driver2.get("https://sushihe5.es/login-email")
for i in tqdm(range(100)):
    password = randomPasswordGenerator()
    driver1.get("https://account.getagil.com/signin")
    loginCL(email, password, driver1,i)
    loginES(email, password, driver2,i)
driver1.close()
driver2.close()