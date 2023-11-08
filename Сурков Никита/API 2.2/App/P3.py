from flask import Flask, render_template, request, jsonify, app
from flask_mysqldb import MySQL
from App.Connect import *
import json
def P3():
    cursor = mysql.connection.cursor()
    cursor.execute('''
    SELECT 
        `sportsmen`.`FIO_Sportsmen` AS `FIO_Sportsmen`
    FROM
        `sportsmen`
    WHERE
        (`sportsmen`.`Number_of_trainers` = '1') ''')
    my_result = cursor.fetchall()
    data_list = json.dumps(my_result, ensure_ascii=False)
    return data_list