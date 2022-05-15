import requests
import json
import os
from generate_user import *
from api_mail import generateEmail
import unicodedata

def PasswordTestES(url: str, password_length: int) -> None:
    mail = generateEmail()
    password = randomPasswordEmojiGenerator(password_length)
    body = {
        "returnSecureToken": True,
        "email": mail,
        "password": password
    }
    domain = "hito_iv/ES"
    if not os.path.exists(domain):
        os.makedirs(domain)
    with open(domain+"/mail.txt", "w", encoding="utf-8") as f:
        f.write(mail)
    with open(domain+"/password.txt", "w", encoding="utf-8") as f:
        f.write(password)
    res = requests.post(url, json=body)
    if "error" in res.json():
        print(res.json()["error"]["message"])
    else:
        print("Success!")
        with open(domain+"/response.txt", "w", encoding="utf-8") as f:
            f.write(str(res.json()))

def PasswordTestCL(url: str, password_length: int) -> None:
    nombre = randomNameGenerator()
    apellido = randomNameGenerator()
    mail = generateEmail()
    telefono = randomNumberGenerator()
    password = randomPasswordGeneratorLength(password_length)
    body = {
        "Nombre": nombre,
        "Email": mail,
        "Telefono": telefono,
        "Password": password,
        "IdNacionalidad": 39, # Chile
        "login": True,
        "AppKey": "0f1b9cb676d8bb350e6ab0de2d32532a" # Código del cliente de getAgil.com, básicamente el restaurant que utiliza el servicio de getAgil.
    }
    domain = "hito_iv/CL"
    if not os.path.exists(domain):
        os.makedirs(domain)
    with open(domain+"/mail.txt", "w", encoding="utf-8") as f:
        f.write(mail)
    with open(domain+"/password.txt", "w", encoding="utf-8") as f:
        f.write(password)
    res = requests.post(url, json=body)
    print(res.json()["message"])
    with open(domain+"/response.txt", "w", encoding="utf-8") as f:
        f.write(str(res.json()))
    return res.json()["message"]

PasswordTestES("https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAhj24Tdnxfr37EDXimO_tA-Cl6RQeMqCc",1000000)
for i in range (257,0,-1):
    if PasswordTestCL("https://lambda.getagil.com/prod-auth/register",i) == "No es posible registrar al usuario":
        print("Password length: "+str(i))
    else:
        print("Password length: "+str(i)+" - Success!")
        break

