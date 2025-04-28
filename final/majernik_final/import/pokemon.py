# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd

df = pd.read_csv('../data/pokemon.csv')
df = df[['id','identifier','height','weight','base_experience']].drop_duplicates()
df = df.rename(columns={'id': 'ID', 'identifier': 'Name', 'height' : 'Height', 'weight' : 'Weight', 'base_experience':'Experience'})

db = ('../teambattle.db')

try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    with open('../data/sql/pokemon.sql', 'r') as file:
        pokemon = file.read()
    c.executescript(pokemon)
    df.to_sql(name='POKEMON', con=conn, if_exists='replace', index=False)
    conn.commit()
    c.execute("SELECT * FROM POKEMON LIMIT 5;")
    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()
    
except Exception as e:
    print("Issue connecting to pokemon df in pokemon.py", e)

del df 
