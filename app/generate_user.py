import random
def randomNumberGenerator():
    phone = "9"
    for i in range(8):
        phone += str(random.randint(0, 9))
    return phone
def randomNameGenerator():
    name = ""
    for i in range(random.randint(3, 10)):
        name += chr(random.randint(65, 90))
    return name
def randomPasswordGenerator():
    password = ""
    for i in range(random.randint(6, 10)):
        password += chr(random.randint(65, 90))
    for i in range(random.randint(6, 10)):
        password += chr(random.randint(97, 122))
    for i in range(random.randint(6, 10)):
        password += str(random.randint(0, 9))
    for i in range(random.randint(6, 7)):
        password += chr(random.randint(45, 47))
    return password