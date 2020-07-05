import pymysql
import pandas as pd

# personal config
file_path = 'C:/Users/Tung Linh/Desktop/D4E_premier_league/data folder' #'your git folder path'
user = 'root' #"your username"
pw = 'Nsi668888' #"your password"

# create sql engine
client = pymysql.connect(
        host='localhost',
        user=user,
        password=pw,
        cursorclass=pymysql.cursors.DictCursor)

cursor = client.cursor()
table = 'country'
table = pd.read_csv(f'{file_path}/{table}.csv')

cursor.execute('CREATE DATABASE IF NOT EXISTS premier_league')
cursor.execute('''
	CREATE TABLE IF NOT EXISTS premier_league.country (
		countryId VARCHAR(255) PRIMARY KEY,
		countryName VARCHAR(255)
		)
	''')
for i in range(len(table)):
	cursor.execute(f'''
		INSERT INTO premier_league.country (
			`countryId`,
			`countryName`)
		VALUES (
			'{table['countryId'][i]}',
			'{table['countryName'][i]}'
			);
		''')
client.commit()
