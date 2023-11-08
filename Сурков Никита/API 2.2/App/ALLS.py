from flask import Flask, render_template, request, jsonify, app
from flask_mysqldb import MySQL
from App.Connect import *
import json
def AllSportsmens():
    cursor = mysql.connection.cursor()
    cursor.execute(''' select FIO_Sportsmen from sportsmen ''')
    my_result = cursor.fetchall()
    data_list = json.dumps(my_result, ensure_ascii=False)
    return data_list