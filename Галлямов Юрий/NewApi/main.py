from app import app
from app.Controllers.UserController import user_bp
from app.Controllers.ConversationController import conversation_bp
from app.Controllers.MessageController import message_bp
from app.Controllers.ReportController import report_bp


app.register_blueprint(user_bp)

app.register_blueprint(conversation_bp)

app.register_blueprint(message_bp, url_prefix='/conversation')

app.register_blueprint(report_bp)

if __name__ == "__main__":
    app.run("localhost", 5000)
