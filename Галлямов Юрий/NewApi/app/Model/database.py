from flask_sqlalchemy import SQLAlchemy
from app import app

# Создание экземпляра SQLAlchemy
db = SQLAlchemy(app)
