import sqlite3

# create databases for system
connect = sqlite3.connect('Poker.sqlite')
db_cursor = connect.cursor()

# create db tables
db_cursor.executescript('''
    CREATE TABLE Player (
        id INTEGER NOT NULL PRIMARY KEY UNIQUE,
        name TEXT,
        note_player TEXT VARCHAR(255));
	
    CREATE TABLE Session (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	player_id INTEGER,
	begin DATETIME,
	end DATETIME,
        game VARCHAR(5),
        stakes VARCHAR(5),
	cash_in INTEGER,
	cash_out INTEGER,
	note_session VARCHAR(255));
    
    CREATE TABLE Xlation (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        field VARCHAR(15),
        value VARCHAR(15),
        description VARCHAR(30));
        ''')

# save and close db
connect.commit()
connect.close()
