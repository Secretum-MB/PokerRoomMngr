#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 22:04:09 2017

"""

#  create the high level classes for the program
#  Will there be interaction between the two classes? does table need to limit players in seat

from datetime import datetime

class Table:
    table_identification = 1
    def __init__(self):
        self.table_number = Table.table_identification
        self.game_type = 'Cash'
        self.size = None
        self.location = None
        self.seat_count = 8
        self.stakes = None
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
    
    def set_TableSize(self, size):
        self.size = size
    def set_TableLocation(self, location):
        self.location = location
    def set_TableSeatCount(self, delta):
        self.seat_count += delta
    def set_TableStakes(self, stakes):
        self.stakes = stakes
    def set_TableGameType(self, game_type):
        self.game_type = game_type


class Player:
    def __init__(self, player_id, player_name, player_notes=None):
        self.player_id = player_id
        self.player_name = player_name
        self.player_notes = player_notes
        self.session_notes = None
        self.logon = datetime.now()
        self.logoff = None
        self.buy_in = None
        self.cash_out = None
        # table/seat stuff
        
    def get_PlayerId(self):
        return self.player_id
    def get_PlayerName(self):
        return self.player_name
    def get_PlayerNotes(self):
        return self.player_notes
    def get_PlayerSessionNotes(self):
        return self.session_notes
    def get_PlayerLogon(self):
        return self.logon
    def get_PlayerLogoff(self):
        return self.logoff
    def get_PlayerBuyIn(self):
        return self.buy_in
    def get_PlayerCashOut(self):
        return self.cash_out

    def set_PlayerName(self, name):
        self.player_name = name # we only want to allow this for non-member guests
    def set_PlayerNotes(self, note):
        try:    self.player_notes += note
        except: self.player_notes = note
    def set_PlayerSessionNotes(self, note):
        try:    self.session_notes += note
        except: self.session_notes = note
    def set_PlayerLogoff(self):
        self.logoff = datetime.now()
    def set_PlayerBuyIn(self, amount):
        try:    self.buy_in += amount
        except: self.buy_in = amount
    def set_PlayerCashOut(self, amount):
        self.cash_out = amount  # Going south allowed?
    
    
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















mathias = Player(1,'Mathias')





    
