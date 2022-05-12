from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from config import set_chrome_options
from api_mail import readMails, readMail
from password import changePasswordCL

def registerCL(firstname: str, lastname: str, email: str, phone: str, password: str, password2: str) -> None:
    # Print selenium version
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1024, 768)
    driver.get("https://account.getagil.com/signup")
    time.sleep(1)
    domain = "hito_iii/test_register_CL"
    if not os.path.exists(domain):
        os.makedirs(domain)
    try:
        input_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))
        input_lastName = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lastName")))
        input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
        input_phone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "phone")))
        input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        input_password2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password2")))
        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/form/button")))
        input_name.click()
        input_name.send_keys(firstname)
        input_lastName.click()
        input_lastName.send_keys(lastname)
        input_email.click()
        input_email.send_keys(email)
        input_phone.click()
        input_phone.send_keys(phone)
        input_password.click()
        input_password.send_keys(password)
        input_password2.click()
        input_password2.send_keys(password)
        time.sleep(1)
        driver.save_screenshot(domain+"/screenshot1.png")
        submit_button.click()
        time.sleep(5)
        driver.save_screenshot(domain+"/screenshot2.png")
        input_verification_code= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "code")))
        input_verification_code.click()
        mails = readMails(email)
        verification_code = (readMail(email, mails[0]["id"])["body"]).split("<p style=\"font-size:24px\">")[1].split("</p>")[0]
        input_verification_code.send_keys(verification_code)
        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/form/button")))
        time.sleep(1)
        submit_button.click()
        driver.save_screenshot(domain+"/screenshot3.png")
        time.sleep(8)
        # print actual url
        driver.save_screenshot(domain+"/screenshot4.png")
        changePasswordCL(password2, driver)

    finally:
        driver.close()
def registerES(name: str, email: str, password: str) -> None:
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1920,1080)
    driver.get("https://sushihe5.es/login-email")
    time.sleep(1)
    domain = "hito_iii/test_register_ES"
    if not os.path.exists(domain):
        os.makedirs(domain)

    try:
        driver.save_screenshot(domain+"/screenshot1.png")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login-email/form/div/div[1]/div/div/label[2]"))).click()
        input_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login-email/form/div/div[3]/div[1]/input")))
        input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login-email/form/div/div[4]/div[1]/input")))
        input_pass1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login-email/form/div/div[5]/div[1]/input")))
        input_pass2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login-email/form/div/div[6]/div[1]/input")))
        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login-email/form/div/div[7]/button")))
        input_name.click()
        input_name.send_keys(name)
        input_email.click()
        input_email.send_keys(email)
        input_pass1.click()
        input_pass1.send_keys(password)
        input_pass2.click()
        input_pass2.send_keys(password)
        submit_button.click()
        time.sleep(1)
        driver.save_screenshot(domain+"/screenshot2.png")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/bs-navbar/nav/div/ul[2]/app-user-menu/li/a"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/bs-navbar/nav/div/ul[2]/app-user-menu/li/div/a[1]"))).click()
        time.sleep(2)
        driver.save_screenshot(domain+"/screenshot3.png")

    finally:
        driver.close()

        

