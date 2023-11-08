from app.Model.database import db

class Conversation(db.Model):
    ID_Conversation = db.Column(db.Integer, primary_key=True)
    Title_Conversation = db.Column(db.String, nullable=False)
    Date_Of_Creation = db.Column(db.DateTime, nullable=False)
    Login_Creator = db.Column(db.String, db.ForeignKey('user.Login_User'), nullable=False)
    Type_Conversation = db.Column(db.Boolean, nullable=False)
    Avatar = db.Column(db.String, nullable=False)

    # Отношения
    composition = db.relationship('CompositionOfTheConversation', backref='conversation', lazy='dynamic')