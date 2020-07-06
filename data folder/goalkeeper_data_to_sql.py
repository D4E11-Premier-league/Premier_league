import pymysql
import pandas as pd 
mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '', #your password 
    cursorclass = pymysql.cursors.DictCursor
)

cursor = mysql_client.cursor()

file_path = '' #yourPath
table_name = 'goalkeeper_data'
table = pd.read_csv(f'{file_path}/{table_name}.csv')

# cursor.execute('CREATE DATABASE IF NOT EXISTS premier_league')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS premier_league.goalkeeper_data (
                playerId INT(11) PRIMARY KEY,
                cleanSheet INT(11),
                goalsConceded INT(11),
                saves INT(11),
                penaltySave INT(11),
                punches INT(11),
                totalHighClaim INT(11),
                totalKeeperSweeper INT(11),
                keeperThrows INT(11),
                goalKicks INT(11),
        FOREIGN KEY(playerId) REFERENCES premier_league.players_info(playerId)
                )
        ''')

for i in range(len(table)):
        cursor.execute(f'''
                INSERT INTO premier_league.goalkeeper_data (
                        `playerId`,
                        `cleanSheet`,
                        `goalsConceded`,
                        `saves`,
                        `penaltySave`,
                        `punches`,
                        `totalHighClaim`,
                        `totalKeeperSweeper`,
                        `keeperThrows`,
                        `goalKicks`)
                VALUES (
                        {table['playerId'][i]},
                        {table['cleanSheet'][i]},
                        {table['goalsConceded'][i]},
                        {table['saves'][i]},
                        {table['penaltySave'][i]},
                        {table['punches'][i]},
                        {table['totalHighClaim'][i]},
                        {table['totalKeeperSweeper'][i]},
                        {table['keeperThrows'][i]},
                        {table['goalKicks'][i]}
                        );
                ''')

mysql_client.commit()