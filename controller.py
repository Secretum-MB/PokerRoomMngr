import db_launch as db

from datetime import datetime as date

id = 1554831
name = 'Mathias'
note = 'Shark! Watch out. Stay away!'

# db.cur.execute('INSERT INTO Player (id, name, note_player) VALUES (?, ?, ?)', (id, name, note, ))

#db.cur.execute('INSERT INTO Session (player_id, begin, end, cash_in, cash_out, note_session) VALUES (?, ?, ?, ?, ?, ?)', 
#						(1, date.now() ,date.now(), 300, 800, 'reg', ))


for row in db.cur.execute('SELECT * FROM Player'):
	print(row)


db.conn.commit()
db.conn.close()