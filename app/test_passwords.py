import requests
import json
from generate_user import *

# Request: POST https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAhj24Tdnxfr37EDXimO_tA-Cl6RQeMqCc

res = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyAhj24Tdnxfr37EDXimO_tA-Cl6RQeMqCc")
print(res.text)