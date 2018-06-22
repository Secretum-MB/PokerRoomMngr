# classes.py

#  create the high level classes for the program

from datetime import datetime

class Table:
    table_identification = 1
    def __init__(self, game_type, stakes=None):
        self.table_number = Table.table_identification
        self.game_type = game_type
        self.size = None
        self.location = None
        self.seat_count = 8
        self.seat_status = [0 for i in range(self.seat_count)]
        self.seat_occupant = [None for i in range(self.seat_count)]
        self.stakes = stakes
        Table.table_identification += 1

    def get_TableNumber(self):
        return self.table_number
    def get_TableSize(self):
        return self.size
    def get_TableLocation(self):
        return self.location
    def get_TableSeatCount(self):
        return self.seat_count
    def get_TableStakes(self):
        return self.stakes
    def get_TableGameType(self):
        return self.game_type
    def get_SeatStatus(self, seat):
        return self.seat_status[seat]
    def get_SeatOccupant(self, seat):
        try:
            return self.seat_occupant[seat].get_PlayerName()
        except: return None

    def set_TableSize(self, size):
        self.size = size

    def set_TableLocation(self, location):
        self.location = location
    def set_TableSeatCount(self, delta):
        self.seat_count += delta
        if delta > 0:
            self.seat_status.extend([0 for i in range(delta)])
            self.seat_occupant.extend([None for i in range(delta)])
        else:
            for _ in range(abs(delta)):
                self.seat_status.pop()
                self.seat_occupant.pop()

    def set_SeatOccupant(self, seat, occupant):
        self.seat_occupant[seat-1] = occupant
    def set_TableStakes(self, stakes):
        self.stakes = stakes
    def set_TableGameType(self, game_type):
        self.game_type = game_type
    def set_SeatStatus(self, seat):
        self.seat_status[seat-1] = (self.seat_status[seat-1] + 1) % 2

    def __str__(self):
        return 'tbl#: ' + str(self.get_TableNumber()) + '\n' +\
            'gameTyp: ' + str(self.get_TableGameType()) + '\n' +\
            'stakes: ' + str(self.get_TableStakes()) + '\n' +\
            'occupants: ' + ', '.join([str(self.get_SeatOccupant(i)) for i in range(len(self.seat_occupant))]) + '\n' +\
            'seat_stat: ' + ', '.join([str(self.get_SeatStatus(i)) for i in range(len(self.seat_occupant))]) + '\n' +\
            '#_seats: ' + str(self.get_TableSeatCount()) + '\n' +\
            'size: ' + str(self.get_TableSize()) + '\n' +\
            'location: ' + str(self.get_TableLocation()) + '\n'


class Member_Player:
    def __init__(self, player_id, player_name, player_notes=None):
        self.player_id = player_id
        self.player_name = player_name
        self.player_notes = player_notes
        self.session_notes = None
        self.session_id = None
        self.logon = datetime.now()
        self.logoff = None
        self.buy_in = None
        self.cash_out = None
        self.table_seat = None

    def get_PlayerId(self):
        return self.player_id
    def get_PlayerName(self):
        return self.player_name
    def get_PlayerNotes(self):
        return self.player_notes
    def get_PlayerSessionNotes(self):
        return self.session_notes
    def get_PlayerSessionId(self):
        return self.session_id
    def get_PlayerLogon(self):
        return self.logon
    def get_PlayerLogoff(self):
        return self.logoff
    def get_PlayerBuyIn(self):
        return self.buy_in
    def get_PlayerCashOut(self):
        return self.cash_out
    def get_PlayerTableSeat(self):
        return self.table_seat

    def set_PlayerName(self, name):
        self.player_name = name # we may need to create an initial association
    def set_PlayerNotes(self, note):
        try:    self.player_notes += ' ' + note
        except: self.player_notes = note
    def set_PlayerSessionNotes(self, note):
        try:    self.session_notes += ' ' + note
        except: self.session_notes = note
    def set_PlayerSessionId(self, Id):
        self.session_id = Id
    def set_PlayerLogoff(self):
        self.logoff = datetime.now()
    def set_PlayerBuyIn(self, amount):
        try:    self.buy_in += amount
        except: self.buy_in = amount
    def set_PlayerCashOut(self, amount):
        self.cash_out = amount
    def set_PlayerTableSeat(self, table_seat):
        self.table_seat = table_seat

    def __str__(self):
        return 'PlyId: ' + str(self.get_PlayerId()) + '\n' +\
            'PlyName: ' + str(self.get_PlayerName()) + '\n' +\
            'PlyNotes: ' + str(self.get_PlayerNotes()) + '\n' +\
            'PlySessionNote: ' + str(self.get_PlayerSessionNotes()) + '\n' +\
            'PlySessionId: ' + str(self.get_PlayerSessionId()) + '\n' +\
            'SessionLogon: ' + str(self.get_PlayerLogon()) + '\n' +\
            'SessionLogoff: ' + str(self.get_PlayerLogoff()) + '\n' +\
            'SessionBuy: ' + str(self.get_PlayerBuyIn()) + '\n' +\
            'SessionCashOut: ' + str(self.get_PlayerCashOut()) + '\n' +\
            'SessionTbl/Seat: ' + str(self.get_PlayerTableSeat()[0].get_TableNumber()) +\
                ' / ' + str(self.get_PlayerTableSeat()[1]) + '\n'


class Non_Member_Player():
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_notes = None
        self.logon = datetime.now()
        self.buy_in = None

    def get_PlayerName(self):
        return self.player_name
    def get_PlayerNotes(self):
        return self.player_notes
    def get_PlayerLogon(self):
        return self.logon
    def get_PlayerBuyIn(self):
        return self.buy_in

    def set_PlayerName(self, name):
        self.player_name = name
    def set_PlayerNotes(self, note):
        self.player_notes = note #what if they add more notes in same session
    def set_PlayerBuyIn(self, amount):
        try:    self.buy_in += amount
        except: self.buy_in = amount


    # we want to store for this player his logon time, his cum buy ins, and his name, player note
    # we will not be saving any of this data
    # will he have a player id?



