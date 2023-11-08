from app.Model.database import db

class ContactsUser(db.Model):
    ID_Contacts = db.Column(db.Integer, primary_key=True)
    Login_Contacts = db.Column(db.String, db.ForeignKey('user.Login_User'), primary_key=True, unique=True, nullable=False)