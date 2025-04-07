# -*- coding: utf-8 -*-
import sqlite3

dbStudent = 'data/student.db'
dbTeacher = 'data/teacher.db'
dbClass = 'data/class.db'
dbs = [dbStudent, dbTeacher, dbClass]

createStudent = "CREATE TABLE IF NOT EXISTS STUDENT (ID integer, name text, email text, phone integer, year integer, status text);"
createTeacher = "CREATE TABLE IF NOT EXISTS TEACHER (ID integer, name text, email text, phone integer);"
createClass = "CREATE TABLE IF NOT EXISTS CLASS (ID integer, name text, teacherID integer, department text);"


for db in dbs:
    try:
        conn = sqlite3.connect(db)
    except:
        print(f"{db} failed to connect.")
    finally:
        print(f"{db} connected successfully.")

