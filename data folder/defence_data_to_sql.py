import pymysql
import pandas as pd 
mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = #YourPassword, 
    cursorclass = pymysql.cursors.DictCursor
)

cursor = mysql_client.cursor()

file_path = "C:/Users/andyv/OneDrive/Máy tính/D4E11/epl-project/Premier_league/data folder" #yourPath
table_name = 'defence_data'
table = pd.read_csv(f'{file_path}/{table_name}.csv')

cursor.execute('CREATE DATABASE IF NOT EXISTS premier_league')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS premier_league.defence_data (
                playerId VARCHAR(255) PRIMARY KEY,
                outfielderBlock INT(11),
                interception INT(11),
                totalTackle INT(11),
                lastManTackle INT(11),
                totalClearance INT(11),
                headClearance INT(11),
                aerialWon INT(11),
                own_Goals INT(11),
                errorLeadToGoal INT(11),
                penaltyConceded INT(11),
                fouls INT(11),
                aerialLost INT(11)
                )
        ''')
for i in range(len(table)):
        cursor.execute(f'''
        INSERT INTO premier_league.defence_data (
                `playerId`,
                `outfielderBlock`,
                `interception`,
                `totalTackle`,
                `lastManTackle`,
                `totalClearance`,
                `headClearance`,
                `aerialWon`,
                `own_Goals`,
                `errorLeadToGoal`,
                `penaltyConceded`,
                `fouls`,
                `aerialLost`)
        VALUES (
                {table['playerId'][i]},
                {table['outfielderBlock'][i]},
                {table['interception'][i]},
                {table['totalTackle'][i]},
                {table['lastManTackle'][i]},
                {table['totalClearance'][i]},
                {table['headClearance'][i]},
                {table['aerialWon'][i]},
                {table['own_Goals'][i]},
                {table['errorLeadToGoal'][i]},
                {table['penaltyConceded'][i]},
                {table['fouls'][i]},
                {table['aerialLost'][i]}
                );
        ''')

mysql_client.commit()