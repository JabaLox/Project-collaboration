from app.Model.database import db

class CompositionOfTheConversation(db.Model):
    ID_Conversation = db.Column(db.Integer, db.ForeignKey('conversation.ID_Conversation'), primary_key=True)
    Login_Contacts = db.Column(db.String, db.ForeignKey('user.Login_User'), primary_key=True)

