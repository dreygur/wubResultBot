#!/usr/bin/env python3

"""
Models file for WUB Result bot
Provides Database Acess to main app
Copyright@ Rakibul Yeasin <ryeasin03@gmail.com> <@dreygur>
"""

import os
import json
import sqlite3

class Model:
    """
    Framework-like model feature for our bot.
    We do here some basic db operations like insert, search, remove etc.
    """
    def __init__(self, name):
        """
        Setup the Model.

        :param name: Filename for the sqlite3 database.
        """
        # DB Name
        self.name = name
        # Base Path
        self.base = os.path.abspath(os.path.dirname(__file__))
        self.db = sqlite3.connect(os.path.join(self.base, "db", self.name), check_same_thread=False)
        self.db.row_factory = sqlite3.Row

    def clean(self, data):
        """
        Cleans the data we get to string

        :param data: Data from DB as db object
        """
        self.result = json.dumps([dict(row) for row in data][0])
        self.result = self.result[11:-2].replace('"', '')
        self.result = self.result.replace(', ', "\n")

        return self.result

    def create(self):
        """
        Creates Tables with data in Database.
        Collectss no parameter.
        """
        # Cursor Object
        self.c = self.db.cursor()
        self.c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
        self.c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

        # Save Changes to db
        self.db.commit()

    def fetch(self, roll):
        """
        To fetch desired data from Database

        :param roll: The roll number for the students of whom result should be returned.
        """
        # Result in string
        self.final_result = ""
        # Cursor Object
        self.c = self.db.cursor()
        for i in range(1, 3):
            self.data = self.c.execute("SELECT * FROM `semester%d` WHERE roll = '%d'" % (int(i), int(roll)))
            self.final_result += self.clean(self.data)
        # self.data = self.c.execute("""SELECT * FROM `semester1` AS sm1
        #                                LEFT JOIN `semester2` AS sm2
        #                                ON sm1.id=sm2.id
        #                                LEFT JOIN `semester3` AS sm3
        #                                ON sm1.id=sm3.id
        #                                WHERE sm1.roll = %d""" % int(roll))
        return self.final_result

    def insert(self):
        """
        Inserts data into Database.
        Not implemented yet.
        """
        pass

    def done(self):
        """
        Closes opened Database.
        """
        self.db.close()