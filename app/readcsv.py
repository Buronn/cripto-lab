import pandas as pd

def get_data():
    df = pd.read_csv('https://radioedu.educarex.es/wp-content/uploads/sites/249/2022/02/users.csv')
    # convert to list
    data = df.values.tolist()
    users = []
    for user in data:
        email=user[0].split(';')[1]
        password=user[0].split(';')[2]
        print(email,password)
        users.append((email,password))
    return users


