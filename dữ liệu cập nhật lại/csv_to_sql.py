import pymysql
import pandas as pd
from sqlalchemy import create_engine
import os
l = []

# personal config
file_path = 'C:/Users/Tung Linh/Desktop/D4E_premier_league/dữ liệu cập nhật lại' #'your git folder path'
user = 'root' #"your username"
pw = 'Nsi668888' #"your password"

# create sql engine
client = pymysql.connect(
        host='localhost',
        user=user,
        password=pw,
        cursorclass=pymysql.cursors.DictCursor)

cursor = client.cursor()
cursor.execute('CREATE DATABASE Premier_league')
engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/Premier_league")

# extract data
for root,dirs,files in os.walk(file_path):
    for file in files:
       if file.endswith(".csv"):
           name = file.replace('.csv','')
           file = pd.read_csv(f'{file_path}/{file}')
           file.to_sql(name, con = engine, if_exists = 'append', index=False)
           print(f'transfer {name} done!')


