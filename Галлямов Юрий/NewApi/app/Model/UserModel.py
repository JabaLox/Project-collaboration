from app.Model.database import db
from app.Model.ContactsUserModel import ContactsUser
from app.Model.ConversationModel import Conversation
from app.Model.ReportModel import report
from app.Model.MessageUserModel import MessageUser

class User(db.Model):
    Login_User = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    Password = db.Column(db.String, nullable=False)
    FIO_User = db.Column(db.String, nullable=False)
    Registration_Date = db.Column(db.DateTime, nullable=False)  # Поле для даты регистрации
    Avatar_User = db.Column(db.String)
    Status_User = db.Column(db.Boolean)
    Role = db.Column(db.String)

    # Отношения
    contacts = db.relationship('ContactsUser', backref='user', lazy='dynamic')
    conversations_created = db.relationship('Conversation', backref='creator', lazy='dynamic')

    login_reported = db.relationship("report", backref='reported_by', foreign_keys='[report.Login_UserReported]')
    login_complaimet = db.relationship("report", backref='complainant', foreign_keys='[report.Login_UserComplainant]')


    message_user = db.relationship('MessageUser', backref='user', lazy='dynamic')

    def __init__(self, Login_User, Password, FIO_User, Avatar_User, Status_User, Registration_Date, Role):
        self.Login_User = Login_User
        self.Password = Password
        self.FIO_User = FIO_User
        self.Avatar_User = Avatar_User
        self.Status_User = Status_User
        self.Registration_Date = Registration_Date
        self.Role = Role

