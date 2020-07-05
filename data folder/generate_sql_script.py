import pandas as pd

file_path = 'C:/Users/Tung Linh/Desktop/D4E_premier_league/data folder' #'your git folder path'
user = 'root' #"your username"
pw = 'Nsi668888' #"your password"

db_name = 'premier_league'
table_name = 'players_info'
table = pd.read_csv(f'{file_path}/{table_name}.csv')

cols = list(table.columns)

def generate_db_script (db_name = db_name):
    print(f"cursor.execute('CREATE DATABASE IF NOT EXISTS {db_name}')")

def generate_table_script (db_name = db_name,table_name = table_name,cols = cols):
    print("cursor.execute('''")
    print( f"\tCREATE TABLE IF NOT EXISTS {db_name}.{table_name} (")
    for col in range(len(cols)):
        if col == (len(cols)-1):
            print(f'\t\t{cols[col]} EDIT_DATA_TYPE')
        else:
            print(f'\t\t{cols[col]} EDIT_DATA_TYPE,')
    print("\t\t)")
    print("\t''')")
    

def insert_table_script (db_name = db_name,table_name = table_name,cols = cols):
    print('for i in range(len(table)):')
    print("\tcursor.execute(f'''")
    print( f"\t\tINSERT INTO {db_name}.{table_name} (")
    for col in range(len(cols)):
        if col == (len(cols)-1):
            print(f'\t\t\t`{cols[col]}`)')
        else:
            print(f'\t\t\t`{cols[col]}`,')
    print("\t\tVALUES (")
    for col in range(len(cols)):
        if col == (len(cols)-1):
            print("\t\t\t{table['"+cols[col]+"'][i]}")
        else:
            print("\t\t\t{table['"+cols[col]+"'][i]},")
    print("\t\t\t);")
    print("\t\t''')")
    print("client.commit()")

generate_db_script()
generate_table_script()
insert_table_script()