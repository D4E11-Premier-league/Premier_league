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
table_name = 'attack_data'
table = pd.read_csv(f'{file_path}/{table_name}.csv')

cursor.execute('CREATE DATABASE IF NOT EXISTS premier_league')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS premier_league.attack_data (
                playerId VARCHAR(255) PRIMARY KEY,
                totalScoringAttack INT(11),
                ontargetScoringAttack INT(11),
                hitWoodwork INT(11),
                HeadGoal INT(11),
                PenaltyGoal INT(11),
                FreekickGoal INT(11),
                totalOffside INT(11),
                touches INT(11),
                totalPass INT(11),
                totalThroughBall INT(11),
                totalCross INT(11),
                cornerTaken INT(11)
                )
        ''')
for i in range(len(table)):
    cursor.execute(f'''
        INSERT INTO premier_league.attack_data (
                `playerId`,
                `totalScoringAttack`,
                `ontargetScoringAttack`,
                `hitWoodwork`,
                `HeadGoal`,
                `PenaltyGoal`,
                `FreekickGoal`,
                `totalOffside`,
                `touches`,
                `totalPass`,
                `totalThroughBall`,
                `totalCross`,
                `cornerTaken`)
        VALUES (
                {table['playerId'][i]},
                {table['totalScoringAttack'][i]},
                {table['ontargetScoringAttack'][i]},
                {table['hitWoodwork'][i]},
                {table['HeadGoal'][i]},
                {table['PenaltyGoal'][i]},
                {table['FreekickGoal'][i]},
                {table['totalOffside'][i]},
                {table['touches'][i]},
                {table['totalPass'][i]},
                {table['totalThroughBall'][i]},
                {table['totalCross'][i]},
                {table['cornerTaken'][i]}
                );
        ''')


mysql_client.commit()