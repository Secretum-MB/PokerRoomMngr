import db_launch as db
import classes as structs

from datetime import datetime as date

# you cannot create players like this until you've created tables. 
# these instences will need to be created for functions regarding people to work

def member_session_start(player_id, player_name, cash_in, 
                         table_number, table_seat):
    # initialize player with id and name
    _player = structs.Member_Player(player_id, player_name)
    _player.set_PlayerBuyIn(cash_in)
   
    #gather the existing player notes, if exists. set player notes
    note = db.cur.execute(
        'SELECT note_player FROM Player WHERE id = ?', (player_id, ))
    try: _player.set_PlayerNotes(note.fetchall()[0][0])
    except: pass


    # change seat status at table to occupied (status = 1)
    #this assumes that table instances are already established..
    #will they be assessable within this local scope?


    # initialize a session
    db.cur.execute(
            '''INSERT INTO Session (player_id, begin, cash_in) 
            VALUES (?,?,?)''', (player_id, _player.get_PlayerLogon(),
                               cash_in, )) 
    #need to add game and stakes
    # the table object used in the function parameter 
    #needs to have associated with it a game and its stakes


    db.conn.commit()
    db.conn.close()

    return _player

def non_member_session_start(name, table_no, seat_no):
    pass    



bob = member_session_start(10, 'Bob', 200, 1, 1)

print(bob.get_PlayerId())



#db.conn.commit()
#db.conn.close()
