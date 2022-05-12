from register import registerCL, registerES
from selenium import webdriver
from api_mail import generateEmail
from generate_user import *
from login import loginCL, loginES
from readcsv import get_users
from tqdm import tqdm
if "__main__" == __name__:
    print("Selenium Version: "+str(webdriver.__version__))
    email = generateEmail()
    name = randomNameGenerator()
    password = randomPasswordGenerator()
    phone = randomNumberGenerator()
    with open("generated_users.csv", "a") as f:
        f.write(email+","+password+"\n")
    print("Signing up...")
    registerCL(name, "lastname", email, phone, password, "Aa123.")
    registerES(name, email, password)
    print("Loging in...")
    for user in tqdm(get_users()):
        loginCL(user[0], user[1])
        loginES(user[0], user[1])
    
