from flask import Flask, render_template, request, jsonify, app
from flask_mysqldb import MySQL
from App.Connect import *
import json
def Add():
    data = request.json
    name = data['namerole']
    print(name)
    cursor = mysql.connection.cursor()
    cursor.execute(f'''Insert into role (Name_role ) values ('{name}')''')
    mysql.connection.commit()
    cursor.execute('''select Name_role from role''')
    my_result = cursor.fetchall()
    data_list = json.dumps(my_result, ensure_ascii=False)
    return data_list