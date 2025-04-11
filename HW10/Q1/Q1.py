# -*- coding: utf-8 -*-

import sqlite3

db = 'example.db'

try:
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS POKEMON\
                   (ID INTEGER PRIMARY KEY,\
                    name TEXT NOT NULL UNIQUE,\
                    height INTEGER,\
                    weight INTEGER,\
                    baseXP INTEGER)'
                       );
except:
    print('failure')
finally:
    print('good')    
                   

