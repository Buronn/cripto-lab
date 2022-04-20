from register import registerCL, registerES
from selenium import webdriver
from api_mail import generateEmail
# generate random number of 9, starting with 9
import random
print("Selenium Version: "+str(webdriver.__version__))
def randomNumber():
    phone = "9"
    for i in range(8):
        phone += str(random.randint(0, 9))
    print("telefono:",phone)
    return phone
email = generateEmail()
#registerCL("Pata", "Poto", email, randomNumber, "Ff123.", "Aa123.")
def randomNameGenerator():
    name = ""
    for i in range(random.randint(3, 10)):
        name += chr(random.randint(65, 90))
    return name
registerES(randomNameGenerator(), email, "Ff123.")
