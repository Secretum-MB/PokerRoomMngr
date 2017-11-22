import sqlite3

# creates a db, what happens if dp already exists?// throws error
connect = sqlite3.connect('Testdb.sqlite')

db_cursor = connect.cursor()

db_cursor.executescript('''
	DROP TABLE IF EXISTS Artist;
	
	CREATE TABLE Artist (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT
	)	;''')

connect.commit()
#connect.close()