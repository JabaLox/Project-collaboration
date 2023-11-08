# from app.controllers import *
from app.Model.database import *
from app.Model.MessageUserModel import *
from app.Model.UserModel import *
from flask import request, Blueprint, jsonify
import datetime

message_bp = Blueprint('MessageUser', __name__)

@message_bp.route("/message/", methods=['GET'])
def get_message():
    id_conversation = request.args.get('conversationId')
    message = (
        db.session.query(
            MessageUser.IdMessage,
            MessageUser.Message_content,
            MessageUser.ID_Conversation,
            MessageUser.Login_Sender,
            MessageUser.StatusRead,
            MessageUser.DateSender,
            User.FIO_User,
            Conversation.Avatar
        )
        .join(User, MessageUser.Login_Sender == User.Login_User)
        .join(Conversation, MessageUser.ID_Conversation == Conversation.ID_Conversation)
        .filter(MessageUser.ID_Conversation == id_conversation)
        .all()
    )

    message_list = []

    for message in message:
        message_dict = {
            "IdMessage": message[0],
            "Message_content": message[1],
            "ID_Conversation": message[2],
            "Login_Sender": message[3],
            "StatusRead": message[4],
            "DateSender": message[5].strftime("%d.%m.%Y %H:%M"),
            "Name_Sender": message[6],
            "Avatar": message[7],
        }
        message_list.append(message_dict)

    return jsonify(
        {
            "code": 200,
            "result": message_list
        }
    )

@message_bp.route('/message/', methods=['POST'])
def send_mesage():
    #data_message = request.json

    # login = data_message['login']
    # content = data_message['Message_content']
    # id_conversation = data_message['ID_Conversation']

    login = request.args.get('login')
    content = request.args.get('Message_content')
    id_conversation = request.args.get('ID_Conversation')

    if (login and id_conversation) is None:
        return jsonify({
            "code": 500,
            "message": "An error occurred on the server while sending the message"
        })

    message = MessageUser(id_conversation, content, login,datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),0)

    db.session.add(message)

    db.session.commit()

    return jsonify({
        "code":200,
        "message": "Message is read"
    })

@message_bp.route("/message", methods=["PUT"])
def read_message():
    idMessage = request.args.get("id")

    if idMessage is None:
        return jsonify({
            "code":500,
            "message": "An error occurred on the server while edit status read message"
        })

    message = db.session.query(MessageUser).get(idMessage)

    message.StatusRead = 1

    db.session.commit()

    return jsonify({
        "code": 200,
        "message": "Message is read"

    })


