from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import set_chrome_options
from mail import readMails, readMail
from password import changePassword

def register(firstname: str, lastname: str, email: str, phone: str, password: str, password2: str) -> None:
    # Print selenium version
    print("email: "+email+"\npassword: "+password)
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.set_window_size(1024, 768)
    driver.get("https://account.getagil.com/signup")
    time.sleep(1)
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
        driver.save_screenshot("screenshots/screenshot1.png")
        submit_button.click()
        time.sleep(5)
        driver.save_screenshot("screenshots/screenshot2.png")
        input_verification_code= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "code")))
        input_verification_code.click()
        mails = readMails(email)
        verification_code = (readMail(email, mails[0]["id"])["body"]).split("<p style=\"font-size:24px\">")[1].split("</p>")[0]
        print("codigo verificador: "+verification_code)
        input_verification_code.send_keys(verification_code)
        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/form/button")))
        time.sleep(1)
        submit_button.click()
        driver.save_screenshot("screenshots/screenshot3.png")
        time.sleep(5)
        # print actual url
        print("Registrado correctamente")
        driver.save_screenshot("screenshots/screenshot4.png")
        changePassword(password2, driver)



    finally:
        driver.close()