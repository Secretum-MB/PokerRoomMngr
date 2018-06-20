# controller.py

# this file to contain the functions that performs the actions user takes 
# within the application

# todo:
# find a way to delete a table / player (post session)
# changing tables to one of a different stakes should not be allowed
# how to populate Player table.. at time of session create?
# to incorporate non-member player.. do we have two classe inherit methods from a super class?


import db_launch as db
import classes as structs


def table_create(game_type, stakes=None):
    _table = structs.Table(game_type=game_type, stakes=stakes)
    return _table

def table_change_stakes(table, stakes):
    table.set_TableStakes(stakes)

def table_change_num_players(table, change):
    table.set_TableSeatCount(change)

def table_change_game_type(table, game_type):
    table.set_TableGameType(game_type)
    table.set_TableStakes(None)

def table_change_size():
    pass

def table_change_location():
    pass

def table_remove(table):
    pass

def member_session_start(player_id, player_name, cash_in, 
                         table_seat, game_type, stake):
    # initialize player with id and name
    _player = structs.Member_Player(player_id, player_name)
    _player.set_PlayerBuyIn(cash_in)
   
    # gather the existing player notes, if exists. set player notes
    note = db.cur.execute(
        'SELECT note_player FROM Player WHERE id = ?', (player_id, ))
    try: _player.set_PlayerNotes(note.fetchall()[0][0])
    except: pass
    
    # set table's seat status and sit player down
    table_seat[0].set_SeatStatus(table_seat[1])
    table_seat[0].set_SeatOccupant(table_seat[1], _player)

    # set player's table/seat status
    _player.set_PlayerTableSeat(table_seat)

    # initialize a session
    db.cur.execute(
            '''INSERT INTO Session (player_id, begin, game, stakes, cash_in) 
            VALUES (?,?,?,?,?)''', (player_id, _player.get_PlayerLogon(),
                                    game_type, stake, cash_in, )) 

    # extract from db the session_id and associate it with _player
    session_id = db.cur.execute(
            'SELECT MAX(id) FROM Session WHERE player_id = ?', (player_id, ))
    _player.set_PlayerSessionId(session_id.fetchall()[0][0])

    db.conn.commit()

    return _player


def member_session_addNote(player, note):
    """Create a note that will only be associated with this session."""

    player.set_PlayerSessionNotes(note)
    db.cur.execute(
            '''UPDATE Session SET note_session = (?) WHERE id = (?)
            ''', (note, player.get_PlayerSessionId(), ))

    db.conn.commit()


def member_session_cash_add(player, amount):
    player.set_PlayerBuyIn(amount)
    db.cur.execute(
            '''UPDATE Session SET cash_in = (?) WHERE id = (?)
            ''', (player.get_PlayerBuyIn(),player.get_PlayerSessionId(), ))

    db.conn.commit()


def member_change_table_seat(player, table_seat):
    # update pior table/seat to be vacent
    tbl = player.get_PlayerTableSeat()[0]
    seat = player.get_PlayerTableSeat()[1]
    
    tbl.set_SeatOccupant(seat, None)
    tbl.set_SeatStatus(seat)
    
    # update new table/seat with player
    table_seat[0].set_SeatStatus(table_seat[1])
    table_seat[0].set_SeatOccupant(table_seat[1], player)
    player.set_PlayerTableSeat(table_seat)

    # if attempts to change seat to table with different stakes/game type: must end session and do new


def member_session_end(player, cash_out=None):
    # todo: garbage collect player at end of function
    player.set_PlayerCashOut(cash_out)
    player.set_PlayerLogoff()
    db.cur.execute(
            '''UPDATE Session SET cash_out = (?), end = (?) WHERE id = (?)           
            ''', (cash_out, player.get_PlayerLogoff(), player.get_PlayerSessionId(), ))
    
    db.conn.commit()




# stakes is optional when tournament is selected
tbl_1 = table_create(game_type='cash', stakes='2-5')
tbl_2 = table_create(game_type='cash', stakes='2-5')
tbl_3 = table_create(game_type='cash', stakes='5-10')

# player_id and name will be inherited from user account
# cash/table/seat will be selected upon session start
# game and stake will be inherited from table
bob = member_session_start(player_id=10, player_name='Bob', cash_in=200,
                           table_seat=(tbl_1,1), 
                           game_type=tbl_1.get_TableGameType(),
                           stake=tbl_1.get_TableStakes())







#db.conn.commit()
#db.conn.close()