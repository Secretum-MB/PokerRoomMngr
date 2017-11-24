import db_launch as db
import classes as structs

from datetime import datetime as date

player1 = structs.Player(10, "Bobby")
player1.set_PlayerBuyIn(500)

player1.set_PlayerNotes('Seems like a regular')
player1.set_PlayerSessionNotes('will likely be returning')

db.cur.execute('INSERT INTO Session (player_id, begin, cash_in, note_session) VALUES (?,?,?,?)',
               (player1.get_PlayerId(), player1.get_PlayerLogon(), 
                player1.get_PlayerBuyIn(), player1.get_PlayerSessionNotes(), ))



db.conn.commit()
db.conn.close()