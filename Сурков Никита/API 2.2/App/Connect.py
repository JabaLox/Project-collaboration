from flask import Flask, render_template, request, jsonify, app
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'mysql_server'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kolyan28'
app.config['MYSQL_DB'] = 'API2'
mysql = MySQL(app)