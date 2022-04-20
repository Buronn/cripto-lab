from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def changePasswordCL(newPassword, driver):
    update_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/button[5]")))
    update_password.click()
    time.sleep(1)
    input_pass = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    input_confirm_pass = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmPassword")))
    submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div[1]/button")))
    input_pass.click()
    input_pass.send_keys(newPassword)
    input_confirm_pass.click()
    input_confirm_pass.send_keys(newPassword)
    time.sleep(1)
    driver.save_screenshot("registerCL/screenshot5.png")
    submit_button.click()
    time.sleep(10)
    driver.save_screenshot("registerCL/screenshot6.png")
    return driver

