#!/usr/bin/env python3

"""
    # Models file for WUB Result bot
    # Provides Database Acess to main app
    # Copyright@ Rakibul Yeasin <ryeasin03@gmail.com> <@dreygur>
"""

import os
import sqlite3

class Model:
    def __init__(self, name):
        # DB Name
        self.name = name
        # Base Path
        self.base = os.path.abspath(os.path.dirname(__file__))
        self.db = sqlite3.connect(os.path.join(self.base, self.name), check_same_thread=False)
        self.db.row_factory = sqlite3.Row

    def create(self):
        """
            Creates Tables with data in Database
        """
        self.c = self.db.cursor()
        self.c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
        self.c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

        # Save Changes to db
        self.db.commit()

    def fetch(self, roll):
        """
            To fetch desired data from Database
        """
        self.c = self.db.cursor()
        # self.data = self.c.execute("SELECT * FROM `semester1` WHERE roll = '%s'" % roll)
        self.data = self.c.execute("""SELECT * FROM `semester1` AS sm1
                                       LEFT JOIN `semester2` AS sm2
                                       ON sm1.id=sm2.id
                                       LEFT JOIN `semester3` AS sm3
                                       ON sm1.id=sm3.id
                                       WHERE sm1.roll = %s""" % roll)
        return self.data.fetchall()

    def insert(self):
        """
            Inserts data into Database
        """
        pass

    def done(self):
        """
            Closes opened Database
        """
        self.db.close()