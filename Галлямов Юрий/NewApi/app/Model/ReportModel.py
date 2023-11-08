from app.Model.database import db

class report(db.Model):
    ID_Report = db.Column(db.Integer, primary_key=True, nullable=False)
    Login_UserComplainant = db.Column(db.String, db.ForeignKey('user.Login_User'))
    Login_UserReported = db.Column(db.String, db.ForeignKey('user.Login_User'))
    ID_Conversation = db.Column(db.Integer, db.ForeignKey('conversation.ID_Conversation'))
    Message_context = db.Column(db.Integer, db.ForeignKey('message_user.IdMessage'))
    ID_Violation = db.Column(db.Integer, db.ForeignKey('violation.ID_Violation'))
