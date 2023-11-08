from app.Model.database import db
from app.Model.ReportModel import report

class MessageUser(db.Model):
    IdMessage = db.Column(db.Integer, primary_key=True, nullable=False)
    ID_Conversation = db.Column(db.Integer, db.ForeignKey('conversation.ID_Conversation'))
    Message_content = db.Column(db.String, nullable=False)
    Login_Sender = db.Column(db.String, db.ForeignKey('user.Login_User'))
    DateSender = db.Column(db.DateTime, nullable=False)
    StatusRead = db.Column(db.Boolean, nullable=False)

    reports_message = db.relationship('report', backref='MessageUser', lazy='dynamic')

    def __init__(self, ID_Conversation, Message_content, Login_Sender, DateSender, StatusRead):
        self.ID_Conversation = ID_Conversation
        self.Message_content = Message_content
        self.Login_Sender = Login_Sender
        self.DateSender = DateSender
        self.StatusRead = StatusRead

