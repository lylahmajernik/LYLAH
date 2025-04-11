# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd

df = pd.read_csv('../data/pokemon.csv')

db = 'example.db'


    




try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS POKEMON\
                   (ID INTEGER PRIMARY KEY,\
                    name TEXT NOT NULL UNIQUE,\
                    height INTEGER,\
                    weight INTEGER,\
                    baseXP INTEGER)'
                       );
    for index, row in df.iterrows():
        c.execute("INSERT INTO POKEMON (ID,name,height,weight,baseXP)\
                       VALUES (?,?,?,?,?)",\
                    (row['id'],row['identifier'],row['height'],row['weight'],row['base_experience']))
    
  
    conn.commit()
    conn.close()
   
except Exception as e:
    print('failure', e)

