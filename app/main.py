from register import register
from selenium import webdriver
from mail import generateEmail, readMails, readMail
# generate random number of 9, starting with 9
import random
print("Selenium Version: "+str(webdriver.__version__))
phone = "9"
for i in range(8):
    phone += str(random.randint(0, 9))
print("telefono:",phone)
email = generateEmail()
register("Pata", "Poto", email, phone, "Ff123.", "Aa123.")
