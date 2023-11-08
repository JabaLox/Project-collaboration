from flask import Flask

app = Flask(__name__)

# Настройка подключения к базе данных MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:kolyan28@localhost/messenger_db'



