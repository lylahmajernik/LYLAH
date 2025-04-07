# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, json
import sqlite3

dbStudent = 'data/student.db'
dbTeacher = 'data/teacher.db'
dbClass = 'data/class.db'
dbs = [dbStudent, dbTeacher, dbClass]


createStudent = "CREATE TABLE IF NOT EXISTS STUDENT (ID integer, name text, email text, phone integer, year integer, status text);"
createTeacher = "CREATE TABLE IF NOT EXISTS TEACHER (ID integer, name text, email text, phone integer);"
createClass = "CREATE TABLE IF NOT EXISTS CLASS (ID integer, name text, teacherID integer, department text);"

app = Flask(__name__)

countclasses = []
teachers = []

#EX STUDENT : {"ID":"1","name":"1","email":"1","phone":"1","year":"1","status":"1"}
#EX TEACHER: {"ID":"1","name":"1","email":"1","phone":"1"}
#EX CLASS: {"name":"1","ID":"1","teacherID":"1"}




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#--Student
@app.route('/student', methods=['POST', 'GET', 'DELETE'])
def student():
    data = request.get_json()
#make sure there's data    
    if not data:
            return jsonify({'error': 'Need data'}), 500
#post....    
    if request.method == 'POST':
#make sure required fields, if not, return error of what field needed        
        required_fields = ['ID', 'name', 'email', 'phone', 'year', 'status']
        for field in required_fields:
            if not data.get(field):  
                return jsonify({'error': f'{field} is required'}),500
       
#set up variables for json info
        SID = request.args.get('ID')
        SP = request.args.get('phone')
        getNumber = f"SELECT * FROM STUDENT where ID = {SID}"
        changeNumber = f"UPDATE STUDENT SET phone = {SP} WHERE phone = data['phone']"

        pID = data.get("ID")
        pname = data.get('name')
        pemail = data.get('email')
        pphone = data.get('phone')
        pyear = data.get('year')
        pstatus = data.get('status')
        
        
#insert json values into database         
        try:
            conn = sqlite3.connect(dbStudent)
            c = conn.cursor()
            if SID and SP is not None:
                c.row_factory = sqlite3.Row
                rows = c.fetchall()
                c.execute(getNumber)
                for row in rows:
                    print(row['phone'])
                c.execute(changeNumber)
                for row in rows:
                    print(row['phone'])
                conn.commit()
                return jsonify({f"New Number for Student {SID}":SP})
            c.execute(createStudent)
            q = "INSERT INTO STUDENT(id,name,email,phone,year,status) VALUES('{i}','{n}','{e}','{p}','{y}','{s}')".format(i=pID,n=pname,e=pemail,p=pphone,y=pyear,s=pstatus)
            c.execute(q)
            conn.commit()
            conn.close()
            return jsonify({'Added Student With ID': data["ID"]})
        except Exception as e:
            print(e)
            return jsonify("{'error':'student post'}"),500
    
######################################################
    if request.method == 'DELETE':
        required_fields = ['ID']
        
        deleteMe = data.get('ID')
        
        
        if data.get('ID') is None:
            return 'Enter student ID to delete student'
        
        deleteStudent = f"DELETE FROM STUDENT WHERE ID = {deleteMe};"
        
        try:
            conn = sqlite3.connect(dbStudent)
            c = conn.cursor()
            print(deleteStudent)
            c.execute(deleteStudent)
            conn.commit()
            testData = "SELECT * FROM STUDENT"
            c.execute(testData)
            rows = c.fetchall()
            conn.close()
            for row in rows:
                print(row)
            return jsonify({"Deleted Student with ID": deleteMe})
        except Exception as e:
            print(e)
            return jsonify("{'error':'student delete'}"),500
          
# ######################################################    
    if request.method == 'GET':
        required_fields = ['ID']
        students = []
        getMe = data.get('ID')
        getData = f"SELECT * FROM STUDENT WHERE ID = {getMe}"

        if data.get('ID') is None:
            return 'Enter student ID to get student info'
        
        try:
            conn = sqlite3.connect(dbStudent)
            c = conn.cursor()
            c.execute(getData)
            rows = c.fetchall()
            conn.close()
            for row in rows:
                student = {
                "ID": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "year": row[4],
                "status": row[5]
                }
                students.append(student)
            if len(students) == 0:
                return jsonify({"error":f"no student with ID {getMe} found. "})
            return jsonify({"STUDENT": students})
        except Exception as e:
            print("broken",e)
            




# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






    
# ##--Teacher    
@app.route('/teacher', methods=['POST', 'GET', 'DELETE'])
def teacher():
    data = request.get_json()
    
    if not data:
            return jsonify({'error': 'Need data'}), 500
    
    if request.method == 'POST':
        required_fields = ['ID', 'name', 'email', 'phone']               
        for field in required_fields:
            if not data.get(field):  
                return jsonify({'error': f'{field} is required'}),500
     
        pID = data.get("ID")
        pname = data.get('name')
        pemail = data.get('email')
        pphone = data.get('phone')
        
        try:
            conn = sqlite3.connect(dbTeacher)
            c = conn.cursor()
            c.execute(createTeacher)
            q = "INSERT INTO TEACHER(id,name,email,phone) VALUES('{i}','{n}','{e}','{p}')".format(i=pID,n=pname,e=pemail,p=pphone)
            c.execute(q)
            conn.commit()
            conn.close()
            return jsonify({'Added Teacher With ID': data["ID"]})
        except Exception as e:
            print(e)
            return jsonify("{'error':'teacher post'}"),500
    
# ######################################################
    if request.method == 'DELETE':
        required_fields = ['ID']
        
        deleteMe = data.get('ID')
        
        if data.get('ID') is None:
            return 'Enter teacher ID to delete teacher'
        
        deleteTeacher = f"DELETE FROM TEACHER WHERE ID = {deleteMe};"
        
        try:
            conn = sqlite3.connect(dbTeacher)
            c = conn.cursor()
            print(deleteTeacher)
            c.execute(deleteTeacher)
            conn.commit()
            testData = "SELECT * FROM TEACHER"
            c.execute(testData)
            rows = c.fetchall()
            conn.close()
            for row in rows:
                print(row)
            return jsonify({"Deleted Teacher with ID": deleteMe})
        except Exception as e:
            print(e)
            return jsonify("{'error':'teacher delete'}"),500
          
# ######################################################    
    if request.method == 'GET':
        required_fields = ['ID']
        getMe = data.get('ID')
        getData = f"SELECT * FROM TEACHER WHERE ID = {getMe}"

        if data.get('ID') is None:
            return 'Enter teacher ID to get teacher info'
        
        try:
            conn = sqlite3.connect(dbTeacher)
            c = conn.cursor()
            c.execute(getData)
            rows = c.fetchall()
            conn.close()
            for row in rows:
                teacher = {
                "ID": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3]
                }
                teachers.append(teacher)
            if len(teachers) == 0:
                return jsonify({"error":f"no teacher with ID {getMe} found. "})
            return jsonify({"TEACHER": teachers})
        except Exception as e:
            print("broken",e)
        
       
@app.route('/teacher/<ID>', methods=['GET'])
def teacherid(ID):
    if ID is None:
        return jsonify({"error":"teacher with this ID not found."})
    
    find = f"SELECT * FROM CLASS where teacherID = {ID}"
    
    try:
        conn = sqlite3.connect(dbClass)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(find)
        rows = c.fetchall()
        if not rows:
            return jsonify({"error": "Teacher with this ID not found."})
        conn.close()
        TD = []
        for row in rows:
            TD.append(dict(row))
        return jsonify({
            f"Teacher {ID} Class Count": len(TD),
            f"Teacher {ID} Classes": TD
            })    
    except Exception as e:
        print("broken",e)

        
    
                
          

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    

# ##--Class
@app.route('/class', methods=['POST', 'GET', 'DELETE'])
def classs():
    data = request.get_json()
    
    
    if not data:
            return jsonify({'error': 'Need data'}), 500
    
    if request.method == 'POST':
        required_fields = ['ID', 'name', 'teacherID']
        
        data['department'] = data.get('department', 'Misc')        
       
        for field in required_fields:
            if not data.get(field):  
                return jsonify({'error': f'{field} is required'}),500
        
        
        countclasses.append(data)
       
        pID = data.get("ID")
        pname = data.get('name')
        pteacherID = data.get('teacherID')
        pdepartment = data.get('department')
        
        try:
            conn = sqlite3.connect(dbClass)
            c = conn.cursor()
            c.execute(createClass)
            q = "INSERT INTO CLASS(id,name,teacherID,department) VALUES('{i}','{n}','{t}','{d}')".format(i=pID,n=pname,t=pteacherID,d=pdepartment)
            c.execute(q)
            conn.commit()
            conn.close()
            
            return jsonify({'Added Class With ID': data["ID"]})
        except Exception as e:
            print(e)
            return jsonify("{'error':'class post'}"),500
    
# ######################################################
    if request.method == 'DELETE':
        
        deleteMe = request.args.get('ID')
        
        if deleteMe == None:
            return jsonify({"error":"need query data"})
        
        for c in countclasses:
            if c['ID'] == deleteMe:
                countclasses[:] = [ c for c in countclasses if c.get('ID') != deleteMe]
        
        deleteClass = f"DELETE FROM CLASS WHERE ID = {deleteMe};"
        
        try:
            conn = sqlite3.connect(dbClass)
            c = conn.cursor()
            print(deleteClass)
            c.execute(deleteClass)
            conn.commit()
            testData = "SELECT * FROM CLASS"
            c.execute(testData)
            rows = c.fetchall()
            conn.close()
            for row in rows:
                print(row)
            return jsonify({"Deleted Class with ID": deleteMe})
        except Exception as e:
            print(e)
            return jsonify("{'error':'class delete'}"),500
# ######################################################       
    if request.method == 'GET':
            if request.args.get('count') == 'true':
                return jsonify({'count': len(countclasses)})
            
            classes = []
            required_fields = ['ID']
            getMe = data.get('ID')
            getData = f"SELECT * FROM CLASS WHERE ID = {getMe}"

            if data.get('ID') is None:
                return 'Enter class ID to get student info'
            
            try:
                conn = sqlite3.connect(dbClass)
                c = conn.cursor()
                c.execute(getData)
                rows = c.fetchall()
                conn.close()
                for row in rows:
                    classs = {
                        "ID": row[0],
                        "name": row[1],
                        "teacherID": row[2],
                        "department": row[3]
                        }
                    classes.append(classs)
                if len(classes) == 0:
                    return jsonify({"error":f"no class with ID {getMe} found. "})
                return jsonify({"CLASSES": classes})
            except Exception as e:
                print("broken",e)
                return"boo"
        
            
        
        

        
        
    





app.run(host='0.0.0.0', port=9999, debug=False)


