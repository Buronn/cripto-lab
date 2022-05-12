from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import set_chrome_options
import time
import os

def loginCL(email: str, pasw: str):
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1024, 768)
    driver.get("https://account.getagil.com/signin")
    time.sleep(1)
    domain = "hito_iii/test_login_CL"
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
        driver.save_screenshot(domain+"/1-"+email+".png")
        submit_button.click()
        time.sleep(5)
        driver.save_screenshot(domain+"/2-"+email+".png")
    finally:
        driver.close()
def loginES(email:str, pasw:str):
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1920,1080)
    driver.get("https://sushihe5.es/login-email")
    time.sleep(1)
    domain = "hito_iii/test_login_ES"
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
        driver.save_screenshot(domain+"/1-"+email+".png")
        submit_button.click()
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/bs-navbar/nav/div/ul[2]/app-user-menu/li/a"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/bs-navbar/nav/div/ul[2]/app-user-menu/li/div/a[1]"))).click()
        driver.save_screenshot(domain+"/2-"+email+".png")
    finally:
        driver.close()




    
    